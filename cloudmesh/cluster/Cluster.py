from cloudmesh.mongo.CmDatabase import CmDatabase
from cloudmesh.mongo.DataBaseDecorator import DatabaseUpdate, DatabaseAlter, DatabaseImportAsJson
from cloudmesh.compute.vm.Provider import Provider
from cloudmesh.configuration.Config import Config
from cloudmesh.common.DateTime import DateTime
from cloudmesh.common.debug import VERBOSE
class Cluster:
    """
    cluster test
    cluster build id=ID label
    cluster create cloud=CLOUD n=N label=None
    cluster add id=ID --available LABEL
    cluster remove id=ID --available LABEL
    cluster terminate --available LABEL
    cluster info [verbose=V] [LABEL]
    """

    """
    The 'cm' object manages all properties required by cloudmesh.
    The collection used natively by this class is "cluster-native",
    meaning a cluster that is natively managed by cloudmesh.  Cluster
    managers such as kubernetes may be built on top of this class,
    however should use a collection "cluster-k8"/"cluster-k3", etc.
    Virtualized clusters can be stored in "cluster-virtual".
    The 'status' field should signify the availability of the cluster
    for deployments.  
    TODO signify a distinct field for unused vms that can be reappropriated
    for dynamic vm management

    """
    _default = {
        "name": "TBD",
        "count": 0,
        "cm": {
            "kind": "cluster",
            "driver": None,
            "cloud": None,
            "name": "TBD",
            "updated": "TBD",
            "created": "TBD",
            "status": "available",
            "label": "TBD",
            "group": "cloudmesh",
            "collection": "cluster",
            "modified": "TBD",           
            "creation": 0
        },
        "vms": {}
    }

    def __init__(self, printer=print, name=None):
        """

        :param printer:
        """
        self.printer = printer
        self.config = Config()
        self.provider = Provider(name=(name or self.config['cloudmesh.default.cloud']))

        """
        Database interactions
        - Ensure collection:'cluster' is created
        - 
        """        
        self.db = CmDatabase()
        self.db.connect()
        self.collection = self.db.collection("cluster")
        
        
    def create(self, label, vms=[], n=None, cloud=None):
        """
        create a document attached to cluster label

        TODO: describe


        :param label:
        :param vms:
        :param n:
        :param cloud:
        :return:
        """
        documents = [doc for doc in self.collection.find({'name': label})]
        self.document = documents[-1] if len(documents) > 0 else None
        # get most recent document easily
        if self.document:
            raise ValueError(f"Cluster {label} already exists in database.")
        else:
            self.document = self._default

        self.document.update({
            'name': label
        })
        self.document['cm'].update({
            'created': DateTime.now(),
            'modified': DateTime.now(),
            'updated': DateTime.now(),
        })
        self.add(label=label,vms=vms,n=n,cloud=cloud)
        self.collection.insert_one(self.document)
        return self.document
    
    def update(self, item):
        self.document.update(item)
        self.document['cm'].update({
            'updated': DateTime.now(),
        })
        self.document['count'] = len(self.document['vms'].keys)

    def add(self, label, vms=[], n=None, cloud=None):
        """
        TODO: describe

        :param label:
        :param vms:
        :param n:
        :param cloud:
        :return:
        """
        self.update({'vms': 
                        {f"{label}_{self.document['count']+i}": self.provider.create(
                                                                    name=vm_name,
                                                                    cloud=cloud
                                                                )
                        } for i in range(n)})

        self.update({'vms':
                        {vm_name: self.provider.status(
                                        name=vm_name,
                                        cloud=cloud
                                    )
                        } for vm_name in vms})

    def remove(self, label, vms=None, n=None, cloud=None):
        """
        TODO: describe

        :param label:
        :param vms:
        :param n:
        :param cloud:
        :return:
        """
        self.update({'vms':{k:v for k,v in self.document['vms'] if k not in vms}})
        vms = vms.extend([self.document['vms'].keys().pop() for i in range(n)])
        [self.provider.stop(name=vm_name, cloud=cloud) for vm_name in vms]
        self.update({})
        

    def terminate(self, label, kill=None):
        """
        TODO: describe

        :param label:
        :param kill:
        :return:
        """
        if kill:
            for _, vm in self.document['vms'].items():
                p = Provider(name=vm['cm']['driver'])
                p.stop(name=vm['name'])
        self.collection.delete_many({
            'name': label
        })

    def info(self, verbose=None, label=None):
        """
        TODO: describe

        :param verbose:
        :param label:
        :return:
        """
        def _return_doc_verbosity(doc, verbose=3):
            if verbose==0:
                if type(doc) is dict or type(doc) is list:
                    return "trimmed"

            if type(doc) is list:
                return [
                    _return_doc_verbosity(v, verbose=verbose-1) \
                        for v in doc
                ]

            if type(doc) is dict:    
                return {
                    k:_return_doc_verbosity(v, verbose=verbose-1) \
                        for k,v in doc.items()
                }

            # base case - all non-nested values
            return doc

        return _return_doc_verbosity(self.get_cursor(name=label), verbose=verbose)
    
    def deploy(self, script):
        for vm_name, vm in self.document['vms']:
            vm.ssh(script)

    def get_cursor(self, **kwargs):
        self.document = self.collection.find(kwargs)
        return self.document