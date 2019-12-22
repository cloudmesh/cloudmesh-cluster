from __future__ import print_function
from cloudmesh.shell.command import command, map_parameters, PluginCommand
from cloudmesh.common.console import Console
from cloudmesh.common.util import path_expand
from pprint import pprint
from cloudmesh.common.debug import VERBOSE
from cloudmesh.common.Shell import Shell
import datetime
import textwrap
from cloudmesh.configuration.Config import Config

class ClusterCommand(PluginCommand):

    # noinspection PyUnusedLocal
    @command
    def do_cluster(self, args, arguments):
        """
        ::

		  Usage:
				cluster create --service=SERVIE --provider=PROVIDER --deploy=FILE NAME --n=N
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
              --service     specify hadoop or nomad ....

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

        map_parameters(arguments,
                       'name',
                       'provider',
                       'deploy',
                       'n'
                       )

        clusters = {}

        # can not have /bin/bash
        # nuste read anme from yaml
        # must use dedent

        config = Config()
        user = config["cloudmehs.profile.user"]

        vm_boot = textwrap.dedent(
            f"""
            cms vm boot \
                --name={user}-{arguments.service} \
                --output=json \
                --n={arguments.n}
		    """
        )

        if arguments.create:

            name = arguments.NAME

            Console.info(f"Creating cluster {name}...")

            # BUG: Please use DateTime from cloudmesh to gurantee uniform tiemstamps
            clusters[name] = {
                'created_at': datetime.datetime.now().strftime(
                    "%Y-%m-%D %H:%M:%S"),
                'machines': []
            }
            VERBOSE(clusters)


        elif arguments.add:

            Console.info(
                f"Adding {arguments.NAME} from {arguments.name}")
            # msg is unclear e.g what is from

            cluster_name = arguments.name
            machine_name = arguments.NAME

            if cluster_name not in clusters.keys():
                VERBOSE(clusters)
                raise ValueError(
                    f"{cluster_name} doesn't exist. Create cluster with cms cluster create.")

            if machine_name in clusters[cluster_name]['machines']:
                VERBOSE(clusters)
                raise ValueError(f"{machine_name} already in {cluster_name}")

            clusters[cluster_name]['machines'].append(machine_name)
            VERBOSE(f"Successfully added {machine_name} to {cluster_name}.")

        elif arguments.remove:
            Console.info(
                f"Attempting to remove {arguments.NAME} from {arguments.name}")

        elif arguments.deploy:
            Console.info(
                f"Attempting to deploy {arguments.FILE} from {arguments.name}")

        elif arguments.kill:
            Console.info(f"Attempting to kill {arguments.NAME}")
            Shell()
        elif arguments.list:
            VERBOSE(clusters)

        elif arguments.info:
            Console.info(f"Retriving info for cluster {arguments.NAME}")

        return ""