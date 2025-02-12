# Setting Up Amazon EKS (Elastic Kubernetes Service)

This guide provides step-by-step instructions for installing and configuring Amazon EKS using `eksctl`, along with building and deploying a Dockerized application.

## Prerequisites

Ensure you have the following installed:

- **AWS CLI** (Configure using `aws configure`)
- **kubectl** (For interacting with Kubernetes cluster)
- **eksctl** (For EKS cluster management)
- **Docker** (For building and running containers)

## 1. Install Required Tools

### Install AWS CLI:
```bash
sudo apt update && sudo apt install -y awscli
aws --version
```

### Install kubectl:
```bash
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl
kubectl version --client
```

### Install eksctl:
```bash
curl --silent --location "https://github.com/weaveworks/eksctl/releases/latest/download/eksctl_$(uname -s)_amd64.tar.gz" | tar xz -C /tmp
sudo mv /tmp/eksctl /usr/local/bin
eksctl version
```

## 2. Create an EKS Cluster
```bash
eksctl create cluster --name test-cluster1 \  
    --version 1.28 \  
    --region us-east-1 \  
    --nodegroup-name standard-workers \  
    --node-type t3.small \  
    --nodes 2 \  
    --nodes-min 1 \  
    --nodes-max 2 \  
    --managed
```

## 3. Verify Cluster
```bash
kubectl get nodes
```

## 4. Build and Push Docker Image

### Clone the Repository
```bash
git clone https://github.com/your-repo/flask-rds.git
cd flask-rds
```

### Build Docker Image
```bash
docker build -t flask-app .
```

### Run Docker Container Locally (Optional)
```bash
docker run -d -p 8080:8080 flask-app
```

## 5. Deploy Application on EKS

### Apply Deployment and Service
```bash
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
```

### Verify Pods and Services
```bash
kubectl get pods -w
kubectl get svc
```

## 6. Access the Application

### Get the External LoadBalancer DNS
```bash
kubectl get svc
```

Look for the **EXTERNAL-IP** of your service (LoadBalancer type). Access the application in a browser or via `curl`:
```bash
curl http://<EXTERNAL-IP>:<PORT>
```

## 7. Delete EKS Cluster
```bash
eksctl delete cluster --name test-cluster1
```

---

This completes the setup of EKS, deploying a Dockerized application, and accessing it via DNS. 🎉

