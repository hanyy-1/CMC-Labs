\# Lab 4 — Microservices and Cloud-Native Design



\## Overview

This lab demonstrates a simple microservices architecture using Docker and Docker Compose.



\## Services



\### product-service (Port 5001)

\- `GET /health` - Health check

\- `GET /products/<id>` - Get product by ID



\### order-service (Port 5002)

\- `GET /health` - Health check

\- `POST /orders` - Create new order



\## How to Run



```bash

docker compose up --build -d

