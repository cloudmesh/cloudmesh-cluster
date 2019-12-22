from __future__ import print_function
from cloudmesh.shell.command import command
from cloudmesh.shell.command import PluginCommand
from cloudmesh.common.console import Console
from cloudmesh.common.util import path_expand
from pprint import pprint
from cloudmesh.common.debug import VERBOSE

class ClusterCommand(PluginCommand):

    # noinspection PyUnusedLocal
    @command
    def do_cluster(self, args, arguments):
        """
        ::

		  Usage:
				cluster create --service=SERVIE --provider=PROVIDER --deploy=FILE NAME
				cluster add --name=LABEL NAME
				cluster remove --name=LABEL OTHENAME
				cluster deploy --name=LABEL FILE
				cluster kill NAME
				cluster list
				cluster info NAME
		  		cluster

		  This command allows you to create and interact with an available cluster.

		  Arguments:
			  NAME   	A name/id of a cluster or machine
			  PROVIDER	One of {Nomad, Kubernetes}
			  FILE		Jobfile for given provider

		  Options:
			  --name        specify name (WHAT NAME RENAME TO LABEL?)
			  --provider    specify provider
			  --deploy      specify application to deploy (jobfile)
              --service     specify application to deploy (jobfile)

          Description:

                PLEASE REMOVE ALL TABS TABS IN YOUR MAN PAGE ARE NOT ALLOWED!!!!!!

          		cluster create --service= SERVICE --provider=PROVIDER --deploy=FILE NAME

          		    TBD

				cluster add --name=LABEL NAME

          		    TBD

				cluster remove --name=LABEL OTHENAME

          		    TBD

				cluster deploy --name=LABEL FILE

          		    TBD

				cluster kill NAME

          		    TBD

				cluster list

          		    TBD

				cluster info NAME

          		    TBD

		  		cluster

        """

        VERBOSE(arguments)
