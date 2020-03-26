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

    def __init__(self):
        pass

    def test(self):
        raise NotImplementedError

    def build(self, id=None, label=None):
        raise NotImplementedError

    def create(self, cloud=None, n=None, label=None):
        raise NotImplementedError

    def add(self, id=None, available=None, label=None):
        raise NotImplementedError

    def remove(self, id=None, available=None, label=None):
        raise NotImplementedError

    def terminate(self, available=None, label=None):
        raise NotImplementedError

    def info(self, verbose=None, label=None):
        raise NotImplementedError
