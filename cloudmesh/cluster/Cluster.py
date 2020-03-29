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

    _default_headers = {
        "collection": "clusters",
    }

    document = {
        "label": None,
        "count": 0,
        "vms": []
    }

    def __init__(self, printer=print, config=None):
        self.printer = printer
        self.db = CmDatabase()
        try:
            self.db.connect()
        except:
            self.printer("Can't connect to database.")

        self.provider = Provider()
    
    def load(self, label):
        self.document(self.db.find(collection=self._default_headers['collection'], query=label))

    @property
    def document(self, refresh=False):
        """
        Loads document from database and updates class variable 'document'
        """
        if refresh: self.load(self.document['label'])
        return self.document

    @DatabaseUpdate
    @property.setter
    def document(self, document=None, **kwargs):
        """
        Updates document with given parameters, synced to db.
        Still untested
        """
        self.document = document.update(self._default_headers)
        return self.document

    def create(self, label, vms=[], n=None, cloud=None):
        # create a document attached to cluster label
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
        
        count = self.document['count']
        if n:
            self._boot_vm(
                name=f"{label}_[{count}-{count+i}]",

                )

    def remove(self, label, vms=None, n=None, cloud=None):
        raise NotImplementedError

    def terminate(self, label, kill=None):
        self._update_document()

    def info(self, verbose=None, label=None):
        raise NotImplementedError
    
    def _boot_vm(self, **kwargs):
        # TODO provide implementation for naming vms where a vm already exists in the format LABEL_i
        # ex: if cms cluster create --n=3 TEST is run twice, it should not produce two sets of vms 
        # test_0, test_1, test_2, where the second set fail to create
        self.provider.create(**kwargs)

    @DatabaseUpdate
    def _create_document(self):
        """
        Creates a document attached to a specific cluster
        """
        doc = {label:payload}
        """
        TODO
        What are the headers needed for DatabaseUpdate to attach to the collection needed?
        """
        headers = {}
        return doc

    @DatabaseUpdate
    def _update_document(self):
        """
        Modifies an existing cluster document.
        """
        pass

    def _load_document(self, label):
        """
        Finds a cluster document.
        """
        pass

    @DatabaseUpdate
    def _delete_document(self, label):
        """
        Deletes cluster document.
        """
        pass