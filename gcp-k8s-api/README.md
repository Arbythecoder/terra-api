# Cloud Engineering Assignment

## Overview

This project involves deploying a simple API to Google Cloud Platform (GCP) using Kubernetes (GKE) with Infrastructure as Code (IaC) through Terraform and a CI/CD pipeline with GitHub Actions.

## API Development

- **API**: A simple Flask API that returns the current time in JSON format.
- **Dockerfile**: Containerizes the API for deployment.

## Infrastructure Setup and Deployment

### Terraform Configuration

- **GKE Cluster**: Created with Terraform for deploying the API.
- **NAT Gateway**: Configured to manage egress traffic.
- **IAM Roles and Policies**: Set up for secure access.
- **VPC Networking**: Includes subnets, firewall rules, and security policies.
- **Kubernetes Resources**: Managed using Terraform, including Namespaces, Deployments, Services, ConfigMaps, and Ingress.

### Deploying the API

- **Docker Image**: Built and pushed to Google Container Registry (GCR).
- **Kubernetes Deployment**: Managed through Terraform.

## CI/CD Pipeline

- **GitHub Actions**: Automated pipeline for:
  - Provisioning infrastructure with Terraform.
  - Building and pushing Docker images.
  - Deploying the API to GKE.
  - Verifying API accessibility.

## Running the Project Locally

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/Arbythecoder/terra-api
