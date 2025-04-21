# 🖥️ System Monitoring GUI App (Dockerized)

A lightweight Tkinter-based desktop GUI application to monitor your system's CPU and memory usage — packaged and run inside a Docker container. Built as a demonstration of DevOps and Docker proficiency.

---

## 🚀 Features

- Real-time CPU and memory usage graphs 📊  
- Simple, intuitive GUI built with Python & Tkinter 🐍  
- Fully Dockerized and platform-independent 🐳  
- Ideal showcase project for DevOps and system-level GUI apps  

---

## 🧰 Tech Stack

- **Python 3.10**
- **Tkinter** (GUI)
- **psutil** (System Monitoring)
- **Docker** (Containerization)
- **X11 Forwarding** (GUI in containers)

---

## 🛠️ Prerequisites

- Ubuntu or any Linux distro with GUI and X11
- Docker installed and running
- `xhost` access enabled for GUI apps in Docker

---

## ⚙️ How to Run

### 1. Clone the repository

```bash
git clone https://github.com/Mohammad-Rifat-Khan/Learning-Docker/new/main/Project_01
cd Project_01

```
### 2. Build the Docker Image

```bash
docker build -t system_monitoring_app .

```
### 3. Enable GUI Display Access

```bash
xhost +local:docker

```
### 4. Run the Docker Container with GUI Support

```bash
docker run -it --rm \
  -e DISPLAY=$DISPLAY \
  -v /tmp/.X11-unix:/tmp/.X11-unix \
  -v $HOME/.Xauthority:/root/.Xauthority \
  system_monitoring_app

```
