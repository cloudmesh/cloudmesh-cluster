from cloudmesh.mongo.CmDatabase import CmDatabase
from cloudmesh.mongo.DataBaseDecorator import DatabaseUpdate, DatabaseAlter, DatabaseImportAsJson
from cloudmesh.compute.vm.Provider import Provider

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
            "collection": "cluster-native",
            "modified": "TBD",           
            "creation": 0
        }
    }

    def __init__(self, printer=print):
        """

        :param printer:
        """
        self.printer = printer
        self.db = CmDatabase()
        try:
            self.db.connect()
        except:
            self.printer("Can't connect to database.")

        self.provider = Provider()

        
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

        active_doc = self.document()
        if n:
            new_vms = self._boot_vm(
                name=f"{label}_[0-{i}]",
                cloud=cloud,
                
                )
            vms.extend(new_vms)
        
        if vms:
            self.load(label=label)
            active_doc['count'] += len(vms)
            active_doc['vms'].extend([{'name': vm} for vm in vms])
            # TODO add more data features about vms

        return self.document(document=active_doc)

    def add(self, label, vms=None, n=None, cloud=None):
        """
        TODO: describe

        :param label:
        :param vms:
        :param n:
        :param cloud:
        :return:
        """
        
        count = self.document['count']
        if n:
            self._boot_vm(
                name=f"{label}_[{count}-{count+i}]",

                )

    def remove(self, label, vms=None, n=None, cloud=None):
        """
        TODO: describe

        :param label:
        :param vms:
        :param n:
        :param cloud:
        :return:
        """
        raise NotImplementedError

    def terminate(self, label, kill=None):
        """
        TODO: describe

        :param label:
        :param kill:
        :return:
        """
        self._update_document()

    def info(self, verbose=None, label=None):
        """
        TODO: describe

        :param verbose:
        :param label:
        :return:
        """
        raise NotImplementedError
    
    def _boot_vm(self, **kwargs):
        """
        TODO: describe

        :param kwargs:
        :return:
        """

        # TODO provide implementation for naming vms where a vm already exists
        # in the format LABEL_i

        # ex: if cms cluster create --n=3 TEST is run twice, it should not
        # produce two sets of vms test_0, test_1, test_2, where the second set
        # fail to create

        self.provider.create(**kwargs)

    #@DatabaseUpdate
    def _create_document(self):
        """
        TODO: describe

        :return:
        """
        """
        Creates a document attached to a specific cluster
        """
        doc = {label:payload}
        """
        TODO
        
        What are the headers needed for DatabaseUpdate to attach to the
        collection needed?
        
        """
        headers = {}
        return doc

    #@DatabaseUpdate
    def _update_document(self):
        """
        TODO: describe

        :return:
        """
        """
        Modifies an existing cluster document.
        """
        pass

    def _load_document(self, label):
        """
        TODO: describe

        :param label:
        :return:
        """
        """
        Finds a cluster document.
        """
        pass

    #@DatabaseUpdate
    def _delete_document(self, label):
        """
        TODO: describe

        :param label:
        :return:
        """
        """
        Deletes cluster document.
        """
        pass