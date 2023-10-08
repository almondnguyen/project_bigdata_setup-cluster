# Disclaimer

```
/*
* Your warranty is now void.
*
* I am not responsible for bricked devices, dead SD cards,
* thermonuclear war, or you getting fired because the alarm app failed. Please
* do some research if you have any concerns about features included in this ROM
* before flashing it! YOU are choosing to make these modifications, and if
* you point the finger at me for messing up your device, I will laugh at you.
*/
```

DO NOT RUN THIS ON REAL MACHINE, IT MAY BREAK YOUR LINUX-OS.
---

# Intro
This script is made to automate the installation of a new Hadoop/VM cluster as part of HUST course homework/project.

# Pre-requisites
This script assumes the following:

1. The cluster consists of 3 nodes, 1 namenode at hduser@namenode, 2 datanodes at hduser@datanode1 and hduser@datanode2.
2. All VMs are running on Debian 11 or Ubuntu 22.04 based OSes. May work on other similar distros and absolutely will not work on Arch/Fedora/RHEL.
3. The Internal Network is setup with namenode @ 10.0.0.2/8, datanodes @ 10.0.0.10/8 and 10.0.0.11/8 and gateway 10.0.0.2. For VMWare it'll be the LAN Segment, for VirtualBox it'll be the Internal Network.
4. You can read logs :D

# What it does
- update, debloat, optimize and then setup hostname/routing for Linux
- setup Hadoop configs, including YARN and MapReduce. 

# Usage

[Refer to the Wiki](https://github.com/almondnguyen/project_bigdata_setup-cluster/wiki)

