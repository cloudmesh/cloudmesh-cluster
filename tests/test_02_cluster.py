import pytest
import sys
from cloudmesh.cluster.Cluster import Cluster

test_names = [
    'test_cluster_1',
    'test_cluster_2',
    'test_cluster_3',
    'test_cluster_4'
]

@pytest.fixture()
def db_setup():
    print("setup")
    cl = Cluster(printer=lambda x:print(x, file=sys.stderr))
    yield cl
    print("teardown")
    for doc in cl.cluster.find(
        {'name':name} for name in test_names
    ):
        [cl.provider.stop(name=name, cloud=info['cm']['cloud']) for name, info in doc['vms'].items()]
    cl.collection.remove_many([
        {'name': name} for name in test_names
    ])

class TestCluster:

    def test_create_and_remove_cluster(self, db_setup):
        cl = db_setup
        # Test that doc added to mongo
        cl.create(label="test_cluster_1", n=0)
        assert len([i for i in cl.collection.find({'name':"test_cluster_1"})]) == 1
        # Test that duplicate doc not added
        try:
            cl.create(label="test_cluster_1", n=0)
            assert False
        except ValueError:
            assert True
        # Test that doc removed
        cl.terminate(label="test_cluster_1")
        assert len([i for i in cl.collection.find({'name':"test_cluster_1"})]) == 0
    
    def test_add_and_remove(self, db_setup):
        cl = db_setup
        # create a cluster and invoke the add function by passing a vm/n
        cl.create(label="test_cluster_2", n=1)
        clusters = [i for i in cl.collection.find({'name':"test_cluster_2"})] == 1
        print(clusters)
        assert clusters[0]['count'] == 1 and len(clusters[0]['vms']) == 1
        # add more vms to cluster and check
        cl.add("test_cluster_2", n=2)
        clusters = [i for i in cl.collection.find({'name':"test_cluster_2"})] == 1
        assert clusters[0]['count'] == 3 and len(clusters[0]['vms']) == 3
        # remove vms from cluster
        cl.remove("test_cluster_2", vms=["test_cluster_2_0", "test_cluster_2_1"])
        clusters = [i for i in cl.collection.find({'name':"test_cluster_2"})] == 1
        assert clusters[0]['count'] == 1 and len(clusters[0]['vms']) == 1
        # terminate cluster and remove remaining vms
        cl.terminate("test_cluster_2", kill=True)
        clusters = [i for i in cl.collection.find({'name':"test_cluster_2"})] == 1
        assert len(clusters) == 0


        