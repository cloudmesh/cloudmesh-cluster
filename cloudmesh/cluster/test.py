from cloudmesh.mongo.CmDatabase import CmDatabase

cmdb = CmDatabase()
cmdb.connect()

cluster_virtual = cmdb.collection("cluster-virtual")
print(cluster_virtual)
cluster_virtual.insert_many([{"hello":"world", "test":1}, {"hello":"w", "test":2}])
