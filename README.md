# Devops-pipeline

# Service1 CI/CD Pipeline with Jenkins, Docker, and Kubernetes

This project demonstrates a complete CI/CD pipeline for a microservice called `service1`. The pipeline uses Jenkins to automate the process of building a Docker image, pushing it to Docker Hub, and deploying it to a Kubernetes cluster.

## Table of Contents

- [Project Overview](#project-overview)
- [Technologies Used](#technologies-used)
- [Setup Instructions](#setup-instructions)
  - [Pre-requisites](#pre-requisites)
  - [Clone the Repository](#clone-the-repository)
  - [Docker Setup](#docker-setup)
  - [Kubernetes Setup](#kubernetes-setup)
- [Jenkins Pipeline Stages](#jenkins-pipeline-stages)
- [Output](#output)

## Project Overview

This project showcases the automation of the build and deployment process for a Flask-based microservice using Jenkins, Docker, and Kubernetes. The following steps are automated:
1. Build a Docker image for the service.
2. Push the image to Docker Hub.
3. Deploy the service to a Kubernetes cluster.

## Technologies Used

- **Jenkins**: Continuous Integration and Deployment tool.
- **Docker**: Containerization platform.
- **Kubernetes**: Container orchestration platform.
- **Flask**: Micro web framework written in Python.

## Setup Instructions

### Pre-requisites

Make sure you have the following installed on your local machine or server:
- Docker
- Kubernetes (Minikube, Kind, or a Kubernetes cluster)
- Jenkins
- Git

### Clone the Repository

Clone this repository to your local machine:
git clone https://github.com/ambatibhargavi/microservices-app.git
cd service1-ci-cd


### Docker Setup

![Screenshot 2024-10-19 at 17 31 13](https://github.com/user-attachments/assets/514088a4-fbac-4931-aa28-666f2de19aec)


### Kubernetes Files

![Screenshot 2024-10-19 at 17 41 37](https://github.com/user-attachments/assets/73deb384-9cfb-49ef-b696-3fd86cbe554d)


## Jenkins Pipeline Stages
![Screenshot 2024-10-19 at 18 01 46](https://github.com/user-attachments/assets/2b07865e-56c9-4ddc-94f2-9696505fcb0f)

## Output
<img width="904" alt="Screenshot 2024-10-18 at 22 27 33" src="https://github.com/user-attachments/assets/ef9f5156-d71d-4219-853d-56ea0d9abbd2">
<img width="1300" alt="Screenshot 2024-10-18 at 14 32 01" src="https://github.com/user-attachments/assets/b5e3534e-6d4a-48a7-8f94-202a6c1466b7">
<img width="1104" alt="Screenshot 2024-10-19 at 18 31 38" src="https://github.com/user-attachments/assets/0efda6fa-2916-4cc3-be3f-9d72d46f9696">
<img width="1397" alt="Screenshot 2024-10-19 at 18 32 56" src="https://github.com/user-attachments/assets/194fa45b-d7d8-4807-845b-cd6cc964246a">
<img width="1409" alt="Screenshot 2024-10-19 at 18 38 49" src="https://github.com/user-attachments/assets/a41ccddc-f6bf-4f7f-92f1-8b0844144150">
<img width="1208" alt="Screenshot 2024-10-19 at 18 38 24" src="https://github.com/user-attachments/assets/082be26c-e1fb-455a-986b-89bf3c866de7">
<img width="1170" alt="Screenshot 2024-10-19 at 18 39 13" src="https://github.com/user-attachments/assets/eeafc3c1-0ee4-4003-82a4-8417ca56af10">







