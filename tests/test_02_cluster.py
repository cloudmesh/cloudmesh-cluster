import pytest
import sys
from cloudmesh.cluster.Cluster import Cluster

@pytest.mark.incremental
class TestCluster:
    out = sys.stderr
    cl = Cluster()
    
    def test_create_document(self):
        """ 
        tests that document info is recorded correctly from expected
        
        @param document: expected document
        """
        doc_reqs = {
            "collection": "clusters",
            "count": len(document["vms"])
        }
        tests = [assert v == document(k) for k,v in doc_reqs]
        print(sum(tests)/len(tests), file=self.out)
        return True

    def test_update_document(self):
        """
        Tests that documents are synced correctly with mongo

        @param document: expected document
        """
        pass

    def test_read_document(self):
        """
        
        """

        assert self.test_read_document()

    def test_load_vms_into_provider(self):
        # test creating a cluster when vms are specified

        # test creating a cluster when number is specified
        pass