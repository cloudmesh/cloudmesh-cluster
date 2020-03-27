from __future__ import print_function
from cloudmesh.shell.command import command, map_parameters, PluginCommand
from cloudmesh.common.console import Console
from cloudmesh.common.util import path_expand
from pprint import pprint
from cloudmesh.common.debug import VERBOSE
from cloudmesh.common.parameter import Parameter
from cloudmesh.common.Shell import Shell
import datetime
import textwrap
from cloudmesh.configuration.Config import Config
from cloudmesh.mongo import DataBaseDecorator
from cloudmesh.inventory.inventory import Inventory
from cloudmesh.mongo.CmDatabase import CmDatabase


class ClusterCommand(PluginCommand):

    # noinspection PyUnusedLocal
    @command
    def do_cluster(self, args, arguments):
        """
        ::

          Usage:
            cluster test
            cluster create LABEL [--vms=NAMES... | --n=N]
                           [--cloud=CLOUD]
            cluster add [LABEL] --vms=NAMES...
            cluster remove [LABEL] --vms=NAMES...
            cluster terminate [LABEL] [--vms=NAMES...]
            cluster terminate [LABEL] [--kill]

          This command allows you to create and interact with an available
          cluster of machines.

          Arguments:
            NAMES   Machine names to be added to the cluster.
            LABEL   The label for the cluster.
            CLOUD   Cloud platform to initialize VMs.
            N       Number of instances to request [default: 5]
            V       Verbosity level.

          Options:
            --vms      List of VM names.
            --cloud    Specify cloud platform {AWS, Azure, Openstack}.
            --n        Specify number of VMs to initialize.
            --kill     Terminates all VMs associated with the cluster.
            --verbose  OPTIONAL.  Provides verbosity level for info.

          Description:

            create:

                if vms are specified use them

                if -N is used create new vms and add them the the label
                cluster

                cloudmehs has a cm.group make it cm.gourp=LABEL
                when you start a vm


            add:

                adds the named vpma use Parameter.expand(arguments,vm)


            remoiv terminate:

                same as add


          info:

            cool output with Printer.write

          Description:

            cluster create LABEL [--vms=NAMES... | --n=N] [--cloud=CLOUD]

                Groups VMs into a cluster named LABEL.  If n, cloud are
                specified, then VMs will be booted and added to cluster.

            cluster add [LABEL] --vms=NAMES...

                Adds list of VMs to cluster given their names.

            cluster remove [LABEL] --vms=NAMES...

                Removes list of VMs to cluster given their names.

            cluster terminate [LABEL] [--kill]

                Terminates all instances associated with the cluster, wipes
                cluster data. If --kill is passed, kills all related VMs.

            cluster info [LABEL] [--verbose]

                Retrieves cluster data and machine data associatred with
                cluster.  Verbosity level 1 provides high-level cluster
                information and list of machines associated.  Verbosity level 2
                provides cluster information, machine information and status.
                Verbosity level 3 provides all available information.

        """
        map_parameters(arguments,
                       'id',
                       'label',
                       'cloud',
                       'n',
                       'v',
                       'all',
                       'verbose'
                       )

        # inv = Inventory()
        # inv.read()

        config = Config()
        user = config["cloudmesh.profile.user"]

        cmdb = CmDatabase()

        if arguments.test:
            cmdb = CmDatabase()
            virtual_clusters = cmdb.collection("cluster-virtual")
            print(*[index for index in virtual_clusters.list_indexes()])

        if arguments.build:
            ids, label = arguments.id, arguments.LABEL

            # Builds and stores a cluster connected to existing machine ids
            machines = Parameter.expand(arguments.vms)
            cluster_machines = []
            for i, machine in enumerate(machines):
                cluster_machines.append({
                    f"{machine}_{i}": {
                        "type": "cloud",
                        "cloud": None,
                        "status": "available",
                        "deployment": None
                    }
                })
            print(f"Adding the following machines to cluster-cloud {label}: ")
            VERBOSE(cluster_machines)
            collection = cmdb.collection("cluster-cloud")
            collection.insert_one({label: cluster_machines})

        # # TODO Revise to update to correct mongo create/update
        # cmdb.UPDATE(clusters)

        if arguments.create:
            n, label, cloud = arguments.n, arguments.label, arguments.cloud
            ids = [f"label_{i}" for i in range(n)].join(",")
            starting = [s.run(f"cms vm boot --name={id} --cloud={cloud}") for id
                        in ids]
            s.run(f"cms cluster build --id={ids} {label}")
            print(f"Starting {starting}")

        elif arguments.add:
            pass

        elif arguments.remove:
            pass

        elif arguments.terminate:
            pass

        elif arguments.info:
            v, label = arguments.verbose or arguments.v or None, arguments.LABEL or None
            if label: print(f"Searching for {label}")
            virtual_clusters, cloud_clusters = cmdb.collection(
                "cluster-virtual"), cmdb.collection("cluster-cloud")
            output = {
                'virtual': [i for i in virtual_clusters.find(label)],
                'cloud': [i for i in cloud_clusters.find(label)]
            }

            print(output)
        return ""
