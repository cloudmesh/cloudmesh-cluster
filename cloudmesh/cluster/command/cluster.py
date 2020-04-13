from __future__ import print_function
from pprint import pprint
import datetime
import textwrap
from cloudmesh.common.parameter import Parameter
from cloudmesh.common.Shell import Shell
from cloudmesh.shell.command import command, map_parameters, PluginCommand
from cloudmesh.common.console import Console
from cloudmesh.common.util import path_expand
from cloudmesh.common.debug import VERBOSE
from cloudmesh.configuration.Config import Config

from cloudmesh.inventory.inventory import Inventory
from cloudmesh.mongo.CmDatabase import CmDatabase
from cloudmesh.common.Printer import Printer
from cloudmesh.cluster.Cluster import Cluster
from cloudmesh.common.variables import Variables

class ClusterCommand(PluginCommand):

    # noinspection PyUnusedLocal
    @command
    def do_cluster(self, args, arguments):
        """
        ::

          Usage:
            cluster create LABEL (--vms=NAMES | --n=N) [--cloud=CLOUD]
            cluster (add|remove) LABEL (--vms=NAMES | --n=N) [--cloud=CLOUD]
            cluster terminate LABEL [--kill]
            cluster info LABEL

          This command allows you to create and interact with an available
          cluster of machines.

          Arguments:
            LABEL  The label for the cluster.

          Options:
            --cloud=CLOUD  Specify cloud platform such as AWS, Azure, Openstack.
            --n=N          Specify number of VMs to initialize.
            --vms=NAMES    Machine names to be added to the cluster.
            --kill         TODO: not descripbed what it does

          Description:

            cluster create LABEL [--vms=NAMES | --n=N] [--cloud=CLOUD]

                Groups VMs into a cluster named LABEL.  If n, cloud are
                specified, then VMs will be booted and added to cluster.

            cluster (add|remove) LABEL [--vms=NAMES | --n=N] [--cloud=CLOUD]

                Add or remove VMs from a cluster.  Active sessions on the VM
                will not be modified.  In order to start VMs, pass the number
                of requested machines to --n.

            cluster terminate LABEL [--kill]

                Wipe cluster data and terminate all active deployments to the
                cluster. If --kill is passed, then terminates all VMs through
                Provider class.

            cluster info [LABEL]

                Retrieves cluster data and machine data associated with
                cluster.  Verbosity level 1 provides high-level cluster
                information and list of machines associated.  Verbosity level 2
                provides cluster information, machine information and status.
                Verbosity level 3 provides all available information.

        """
        print(arguments)
        map_parameters(arguments,
                       'vms',
                       'cloud',
                       'n',
                       'kill')

        VERBOSE(arguments)

        config = Config()
        inv = Inventory()
        cmdb = CmDatabase()
        cluster = Cluster(print=Printer.write)

        if arguments.create:
            kwargs = {
                'label': arguments.LABEL,
                'vms': Parameter.expand(arguments.vms) or None,
                'cloud': arguments.cloud or None,
                'n': int(arguments.n) or None
            }
            cluster.create(**kwargs)
            print(cluster.document)

        elif arguments.add:
            pass

        elif arguments.remove:
            pass

        elif arguments.terminate:
            pass

        elif arguments.info:
            variables = Variables()
            v = variables['verbose'] or '10'
            label =arguments.LABEL or None
            if label:
                print(f"Searching for {label}")
            virtual_clusters, cloud_clusters = cmdb.collection(
                "cluster-virtual"), cmdb.collection("cluster-cloud")
            output = {
                'virtual': [i for i in virtual_clusters.find(label)],
                'cloud': [i for i in cloud_clusters.find(label)]
            }

            print(output)
        return ""
