Title: Setting up a GPU Instance on Google Compute Cloud
Date: 2018-08-12 10:20
Category: Infrastructure
Tags: GPU, GCP
Slug: gcp_gpu
Summary: Steps and snippets to get started with a GPU instance on Google Compute Cloud (GCP)

Setting up a GPU instance for deep learning in the Google Cloud has become incredibly easy.
Similar to Deep Learning AMIs for AWS EC2, GCP offers Deep Learning VM Images for Compute Engine ([docs](https://cloud.google.com/deep-learning-vm/docs/)), making basic deployment a one-click procedure from the [Cloud Marketplace](https://console.cloud.google.com/marketplace/details/click-to-deploy-images/deeplearning).

By default, the VM will be set up on a n1-highmem-2 instance (2 vCPUs, 13 GB RAM, 100 GB disk).

You can attach optionally multiple GPUs to the instance (choices: K80, P100, V100).

You can choose between several combinations of pre-installed CUDA versions and deep learning images.

Once the VM is created, it will appear in your [Cloud Console](https://console.cloud.google.com/compute/instances) and can be started from there.

Finally, to access JupyterLab, we need to establish an ssh tunnel with local port forwarding. 

    :::bash
    export INSTANCE_NAME="my-instance"
    gcloud compute ssh $INSTANCE_NAME -- -L 8080:localhost:8080

Using the gcloud cli as shown above also generates a new ssh-key pair if necessary.

### Some More Setup Tasks

    :::bash
    # Enable Persistence Mode
    nvidia-smi -pm 1
    # Disable ECC
    nvidia-smi -e 0
    # Enable GPU Boost Clocks (K80 Specific)
    nvidia-smi -ac 2505,875

