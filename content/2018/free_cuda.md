Title: Remote CUDA Development on a Free K80 GPU on the Google Cloud Platform
Date: 2018-10-12 15:33
Category: Infrastructure
Tags: GPU, GCP
Slug: free_cuda
Summary: Remote CUDA Development Environment Setup

The main goal of this post is to describe how to setup an environment for CUDA development.
The requirments for this setup are:

* Development on a local machine
* Simple, one-click deployment and execution on a remote machine

Note that, this setup does not assume the availability of a CUDA capable device on the local development machine, although this would clearly make debugging more convenient. 

These features are supported by NVIDIA's CUDA IDE [NSight Eclipse Edition](), which ships with the CUDA toolkit.
Additionally, the NSight supports remote debugging and profiling.

In this post, we will show how to set up NSight on Ubuntu 18.04.

Next, we show how to get access to a free Tesla K80 GPU in the Google Cloud and demonstrate our setup in this environment.

## Setting up NSight



## Free GPUs


The free GPU is a feature of [Google colab](colab.research.google.com), Google's Jupyter notebook service for ML/Data Science.
People quickly realized, that the VM running the notebook can be accessed and manipulated, since the notebook is run as root.
For example [this article]() shows how to setup the CUDA compiler on the instance and install a notebook extension that allows the user to write CUDA code in the notebook itself. 

This is however not exactly our goal here. Instead, we require to setup SSH access to the VM.


