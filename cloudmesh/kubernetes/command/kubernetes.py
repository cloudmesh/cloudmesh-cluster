from __future__ import print_function
from cloudmesh.shell.command import command
from cloudmesh.shell.command import PluginCommand
from cloudmesh.kubernetes.api.manager import Manager
from cloudmesh.common.console import Console
from cloudmesh.common.util import path_expand
from pprint import pprint
from cloudmesh.common.debug import VERBOSE

class KubernetesCommand(PluginCommand):

    # noinspection PyUnusedLocal
    @command
    def do_kubernetes(self, args, arguments):
        """
        ::

          Usage:
              kubernetes deploy --cluster=LABEL
			  kubernetes auto LABEL
			  kubernetes info LABEL
			  kubernetes set master --id=[ID] LABEL
			  kubernetes set worker --id=[ID] LABEL
              kubernetes list

          This command does some useful things.

          Arguments:
              LABEL   		Label identifying cluster
			  ID			List of ids to define as master, comma delimited

          Options:
              --cluster 	Specify cluster
			  --id			Specify machine ids

		  Description:
		  	
			  kubernetes deploy --cluster=LABEL
			  	
				  Using an existing cluster spawned by `cms cluster`, deploy kubernetes installation and assign master and worker nodes.

			  kubernetes auto LABEL

			  	  Automatically spawn a cluster made of 5 machines using `cms cluster auto`.

			  kubernetes info LABEL

				  Returns live info returned by kubernetes cluster.

			  kubernetes set master --id=[ID] LABEL
			
				  Sets existing cluster node/s as master.

			  kubernetes set worker --id=[ID] LABEL

				  Sets existing cluster node/s as a worker.

			  kubernetes list
			
				  Lists all available kubernetes clusters.

        """
        arguments.FILE = arguments['--file'] or None 

        VERBOSE(arguments)

        m = Manager()

        if arguments.FILE:
            print("option a")
            m.list(path_expand(arguments.FILE))

        elif arguments.list:
            print("option b")
            m.list("just calling list without parameter")

        Console.error("This is just a sample")
        return ""
