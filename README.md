#### MADE BY Almond(R) ####

# Intro
This script is made to automate the installation of new Hadoop cluster

# Pre-requisites
This script assumes the following:

1. The cluster consists of 3 nodes, 1 namenode at hduser@namenode, 2 datanodes at hduser@datanode1 and hduser@datanode2
2. All VMs are running on Debian 11 or Ubuntu 22.04 based OSes. May work on other similar distros and absolutely will not work on Arch/Fedora/RHEL
3. The Internal Network is setup with namenode @ 10.0.0.2/8, datanodes @ 10.0.0.10/8 and 10.0.0.11/8 and gateway 10.0.0.2. For VMWare it'll be the LAN Segment, for VirtualBox it'll be the Internal Network
4. You can read logs :D

# What it does
- The L0x scripts take care of the Linux side of things (debloat, optimize and then setup hostname/routing)
- The H0x scripts setup Hadoop configs, including YARN and MapReduce. 

# Usage

[Refer to the Wiki](https://github.com/almondnguyen/project_bigdata_setup-cluster/wiki)

