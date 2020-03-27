from cloudmesh.mongo.CmDatabase import CmDatabase
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

    # DO NOT USE TABLE PRINTER HERE, just get dicts

    def __init__(self, printer=print):
        self.printer = printer
        self.db = CmDatabase()
        try:
            self.db.connect()
        except:
            self.printer("Can't connect to database.")

        self.provider = Provider()

    def test(self):
        raise NotImplementedError

    def create(self, label, vms=None, cloud=None, n=None):
        pass

    def add(self, id=None, available=None, label=None):
        raise NotImplementedError

    def remove(self, id=None, available=None, label=None):
        raise NotImplementedError

    def terminate(self, available=None, label=None):
        raise NotImplementedError

    def info(self, verbose=None, label=None):
        raise NotImplementedError
    
    def _boot_vm(self, **kwargs):
        self.provider.create(**kwargs)

    def _create_document(self, label, payload):
        """
        Creates a document attached to a specific cluster
        """
        doc = {label:payload}
        return doc

    def _update_document(self, label, payload):
        """
        Modifies an existing cluster document.
        """
        pass

    def _load_document(self, label):
        """
        Finds a cluster document.
        """
        pass

    def _delete_document(self, label):
        """
        Deletes cluster document.
        """
        pass