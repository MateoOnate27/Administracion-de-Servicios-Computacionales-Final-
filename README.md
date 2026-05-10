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

### 1. Environment Setup
```bash
minikube start --driver=docker
kubectl create namespace ml-project
