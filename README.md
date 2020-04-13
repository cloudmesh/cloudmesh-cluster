Cloudmesh cluster
=============


> **Note:** The README.md page is outomatically generated, do not edit it.
> To modify  change the content in
> <https://github.com/cloudmesh/cloudmesh-cluster/blob/master/README-source.md>
> Curley brackets must use two in README-source.md



[![image](https://img.shields.io/pypi/v/cloudmesh-cluster.svg)](https://pypi.org/project/cloudmesh-cluster/)
[![Python](https://img.shields.io/pypi/pyversions/cloudmesh-cluster.svg)](https://pypi.python.org/pypi/cloudmesh-cluster)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://github.com/cloudmesh/cloudmesh-cluster/blob/master/LICENSE)
[![Format](https://img.shields.io/pypi/format/cloudmesh-cluster.svg)](https://pypi.python.org/pypi/cloudmesh-cluster)
[![Status](https://img.shields.io/pypi/status/cloudmesh-cluster.svg)](https://pypi.python.org/pypi/cloudmesh-cluster)
[![Travis](https://travis-ci.com/cloudmesh/cloudmesh-cluster.svg?branch=master)](https://travis-ci.com/cloudmesh/cloudmesh-cluster)


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

## Features

* Supports hybrid cloud clusters
* Allows for inventory of instances and deployments
* Abstraction in [`cloudmesh.cluster.Cluster`](./cloudmesh/cluster/Cluster.py) allows for added integrations

## Manual

```bash

```


## Tests

 * [test_01_dependencies](tests/test_01_dependencies.py)
 * [test_02_cluster](tests/test_02_cluster.py)
 * [test_03_cli](tests/test_03_cli.py)
