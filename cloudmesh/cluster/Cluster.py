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
    

    def add(self, label, vms=[], n=None, cloud=None):
        """
        TODO: describe

        :param label:
        :param vms:
        :param n:
        :param cloud:
        :return:
        """
        nextVmID = self.document['count']
        for i, vm in enumerate(vms):
            vm_name = f"{label}_{nextVmID}"
            self.document['vms']
            self.provider.create(
                name=f"{label}_{nextVmID}",
                cloud=cloud
            )
        self.document.update({
            'count': n or len(vms),
            'last_created_vm_num': -1,
            'vms': {vm_name:{} for vm_name in vms or []}
        })

    def remove(self, label, vms=None, n=None, cloud=None):
        """
        TODO: describe

        :param label:
        :param vms:
        :param n:
        :param cloud:
        :return:
        """
        pass

    def terminate(self, label, kill=None):
        """
        TODO: describe

        :param label:
        :param kill:
        :return:
        """
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
        raise NotImplementedError
    