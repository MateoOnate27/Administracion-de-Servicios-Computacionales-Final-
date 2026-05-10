# Orchestrating ML Training and Inference with Kubernetes 🚀

This repository contains the final project for the Machine Learning in Production (MLOps) course. The project demonstrates a full ML lifecycle (Training -> Artifact Storage -> Inference) orchestrated using Kubernetes primitives on a Fedora environment.

## 📌 Project Overview

The goal of this lab is to move beyond simple model training and implement a production-ready system where training and inference are decoupled but integrated through Kubernetes orchestration.

### Key Features:
- **Automated Training:** Kubernetes Job for training a Random Forest classifier (Iris Dataset).
- **Persistent Storage:** Use of Persistent Volume Claims (PVC) to store model artifacts.
- **Scalable Inference:** FastAPI-based service deployed with horizontal scaling capabilities.
- **Service Discovery:** NodePort Service for external API access.

---

## 🏗 Architecture

The system is designed with two main pipelines:

1.  **Training Pipeline (Ephemeral):** A Job that runs the training script, saves `model.pkl` to the PVC, and terminates.
2.  **Inference Pipeline (Continuous):** A Deployment that mounts the PVC, loads the model, and serves predictions via HTTP.

---

## 🚀 Getting Started

### Prerequisites
- Fedora Linux / Ubuntu
- Minikube & Kubectl
- Docker

### 1. Execution of the Program
```bash
### 1. Enviromental Setup
minikube start --driver=docker
kubectl create namespace ml-project

### 2. Training the model
# Build the trainer image
cd training/
eval $(minikube docker-env)
docker build -t ml-trainer:v1 .

# Run the training job
kubectl apply -f ../manifests/training-job.yaml

### 3. Deploying Inference
# Build the inference image
cd ../inference/
docker build -t ml-inference:v1 .

# Deploy the service
kubectl apply -f ../manifests/inference-service.yaml

### 4. Testing Predictions
# Get the service URL
minikube service ml-inference-service -n ml-project --url

# Send a sample request
curl -X POST "http://<URL>/predict" \
     -H "Content-Type: application/json" \
     -d '{"input": [[5.1, 3.5, 1.4, 0.2]]}'

### 5. Scalability
# To demonstrate Kubernetes scalability, the inference service can be scaled horizontally:
kubectl scale deployment ml-inference-deployment --replicas=5 -n ml-project

