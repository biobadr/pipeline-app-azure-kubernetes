# python-app-with-azure-kubernetes

This repo is used to Trace an Application Deployed with Azure Kubernetes Service and Azure Pipelines

### Steps

**Create a resource group in Azure Subscription**<br>
`az group create -l eastus -n aks-rg`

**Create Azure k8s cluster**<br>
`az aks create -g aks-rg -n myAKSCluster --node-vm-size Standard_B2s --node-count 1 --generate-ssh-keys`

**Create Azure Container Registry**<br>
`az acr create -g aks-rg -n youruniquename --sku Standard`

**Create Azure Pipelines**<br>
Here you need to create an organization in Azure DevOps and link your Github<br>

**Authenticate your k8s cluster with cloud-shell**<br>
`az aks get-credentials -g aks-rg -n myAKSCluster`

**Get deployments**<br>
`kubectl -n dev get deployments`

**Get pods**<br>
`kubectl -n dev get pods`

**Get services**<br>
`kubectl -n dev get svc`

**Get Horizontal Pod Autoscaler**<br>
`kubectl -n dev get hpa`

**To check the app**<br>
`curl http://[external-ip]:5000`

**To describe pods specification and check logs**<br>
`kubectl -n dev describe pods [pod-name]`
`kubectl -n dev logs [pod-name]`

*We can scale our deployment manually as well as automatically. For automatic scaling, we have defined HPA in YAML which increases one replica of pod whenever the average traffic on the running pod goes beyond 80%. It will increase replica up to the max number we defined in YAML manifest that’s 3 in our case.*

**To manual scale**<br>
`kubectl -n dev scale deployment python-app --replicas=3`
`kubectl -n dev get deployment python-app`

**For interactive UI console of k8s cluster**<br>
`az aks browse -g aks-rg -n myAKSCluster`

**For entering into pods**<br>
`kubectl -n dev exec -it [pod-name] -- /bin/bash`
