from cloudmesh.mongo.CmDatabase import CmDatabase
from cloudmesh.mongo.DataBaseDecorator import DatabaseAlter, DatabaseImportAsJson, DatabaseUpdate
from cloudmesh.common import Console
from cloudmesh.common.Shell import Shell

cm = CmDatabase()

@DatabaseUpdate
def entries():
	