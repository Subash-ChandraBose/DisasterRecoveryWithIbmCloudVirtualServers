# DisasterRecoveryWithIbmCloudVirtualServers
IBM Cloud Private Reference Architecture
This project provides prescriptive guidance on how to efficiently deploy and operate IBM Cloud Private platform in the enterprise. We document the practical approach of planning enterprise private cloud environment, setting up DevOps tool chains, achieving HA/DR, securing the platform and monitoring your private cloud. The project contains assets and best practices to help accelerating the private cloud adoption.


Planning ICP clusters
Sizing ICP
See the following page for recommended sizing of ICP environments: Sizing

Installing IBM Cloud Private
IBM Cloud Private (ICP) supports 64-bit Linux (Red Hat Enterprise Linux & Ubuntu 16.04 LTS) and Linux on Power. We provided some guidance on installing ICP on following virtualization and cloud platforms:

VMware:
Installing ICP with Ubuntu
Installing ICP with RedHat Enterprise
AWS: Installing ICP on AWS
VirtualBox: Installing ICP on VirtualBox
OpenStack: Installing ICP on OpenStack
Install ICP using TerraForm
Terraform Module for provisioning ICP cluster: terraform-module-icp-deploy
IBM Cloud: Deploy ICP Cluster to IBM Cloud
VMware: Deploy ICP to VMware
AWS: Deploy ICP to AWS
OpenStack: Deploy ICP to OpenStack
Azure: Deploy ICP to Azure
Accessing IBM Cloud Private (ICP) through the CLI
Accessing ICp

Installing the Cloud Foundry Environment
Installing ICP Cloud Foundry on-prem

Hyper-V Recommendations
Recommendations for Dynamic Memory Allocation Settings in Hyper-V

High Availability and Resiliency
General High Availability Considerations

Federated ICP clusters
NOTE: This is an early experiential guide on how to federate multiple ICP clusters with the Kubernetes federation control plane utility. Not recommended for production usage.

Setup Highly Available ICP Cluster
Guide and best practice on install and configure a highly available ICP clusters with multiple master nodes, multiple proxy nodes and management nodes.

ICP HA/DR with backup on VMWare Guidance on how to take backup of ICP deployed on VMWare and restore the platform on a DR VMWare site.
