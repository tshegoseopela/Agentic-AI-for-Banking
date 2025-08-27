# Setup for the Retail use case lab

This document contains the documentation for the setup of the environment to prepare for the step-by-step walkthrough of the [Retail use case](../usecases/retail/).

## Introduction

The use case takes you through the creation of tools and agents using the [IBM watsonx Orchestrate Agent Development Kit (ADK)](https://developer.watson-orchestrate.ibm.com/). This toolkit can be installed on a local machine and brings with it the core components of watsonx Orchestrate, as container images that are running in a container runtime like Docker or Rancher. It also installs a CLI that can be used to manage a locally running instance as well as remote instances running in the cloud.

## Environments

To run this lab end to end, you need a number of environments.

### watsonx Orchestrate ADK

As mentioned above, the ADK allows hosting the core Orchestrate components on a developer laptop. For the lab, you can choose if you want to run the ADK on your own laptop or on a virtual machine that will be provided to you by your instructor. 

To run it on your own laptop, you need to install 
- [Docker](https://www.docker.com/products/docker-desktop/) or [Rancher](https://www.rancher.com/products/rancher-desktop)
  - the containers that run as part of the ADK will require ~12GB of memory, so you need to allocate at least that much to the virtual machine hosting the container runtime
- Python 3.11
- Visual Studio Code

Once you have these prerequistites available, you can install the ADK by following the instructions at [the ADK install page](https://developer.watson-orchestrate.ibm.com/getting_started/installing).

You also need to install the watsonx Orchestrate Developer Edition, which is part of the ADK, by following the related [install instructions](https://developer.watson-orchestrate.ibm.com/getting_started/wxOde_setup). However, **DO NOT** set up the .env file as described in the instructions! You will get the values for the various environment variables you need to add from you instructor.

After you created the .env file with the values gven to you, you can follow the instructions to start the server for the first time as documented [here](https://developer.watson-orchestrate.ibm.com/getting_started/wxOde_setup#installing-the-watsonx-orchestrate-developer-edition-with-adk). Note that the first time you run it, it will download all the required container images from the IBM amige reigstry, which will take some time.

### watsonx.ai

For the lab, you will also need access to an IBM watsonx.ai Runtime instance, and specifically, a `deployment space ID` for that instance as well as an `API key` for the IBM Cloud account the instance is running in. You will get both values from your instructor, or additional instructions for how and where to obtain those values. 

The watsonx.ai runtime is used by one of the tools you will create as part of the lab.

### watsonx Orchestrate 

In this lab, you will create a number of components (tools, agents, etc) in your local environment and run and test them there, without the need to access an instance of watsonx Orchestrate in the cloud. However, the last part of the lab describes how you can take the same components and easily deploy and run them on a watsonx Orchestrate SaaS instance. You need such an instance for that part of the lab.

Your instructor will provision both the watsonx.ai and the watsonx Orchestrate instances for you and provide you with the required access details.