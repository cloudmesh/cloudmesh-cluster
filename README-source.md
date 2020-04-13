Cloudmesh cluster
=============

{warning}

{icons}

see cloudmesh.cmd5

* https://github.com/cloudmesh/cloudmesh.cmd5



# Usage
```sh
cluster create LABEL (--vms=NAMES... | --n=N) [--cloud=CLOUD]
cluster (add|remove) LABEL (--vms=NAMES... | --n=N) [--cloud=CLOUD]
cluster terminate LABEL [--kill]
cluster info LABEL [--verbose=V]
```

This command allows you to create and interact with an available
cluster of machines.

## Arguments:  
NAMES  - Machine names to be added to the cluster.  
LABEL  - The label for the cluster.  
CLOUD  - Cloud platform to initialize VMs.  
N      - Number of instances to request [default: 5]  
V      - Verbosity level.  

## Options:  
--cloud    - Specify cloud platform, AWS, Azure, Openstack.  
--n        - Specify number of VMs to initialize.  
--verbose  - Returns information as per verbosity level.  


## Description:

`cluster create LABEL [--vms=NAMES... | --n=N] [--cloud=CLOUD]`  
Groups VMs into a cluster named LABEL.  If n, cloud are specified, then VMs will be booted and added to cluster.

`cluster (add|remove) LABEL [--vms=NAMES... | --n=N] [--cloud=CLOUD]`  
Add or remove VMs from a cluster.  Active sessions on the VM will not be modified.  In order to start VMs, pass the number of requested machines to --n.

`cluster terminate LABEL [--kill]`  
Wipe cluster data and terminate all active deployments to the cluster. If --kill is passed, then terminates all VMs through Provider class.

`cluster info [LABEL] [--verbose]`  
Retrieves cluster data and machine data associated with cluster.  Verbosity level 1 provides high-level cluster information and list of machines.  Verbosity level 2 provides cluster information, machine information and status. Verbosity level 3 provides all available information.

# Features

* Supports hybrid cloud clusters
* Allows for inventory of instances and deployments
* Abstraction in [`cloudmesh.cluster.Cluster`](./cloudmesh/cluster/Cluster.py) allows for added integrations