\# Lab 4 Report — Microservices and Cloud-Native Design



\## 1. Introduction



This lab demonstrates building a cloud-native microservices system using Docker and Docker Compose. The system consists of two services that communicate over HTTP.



\## 2. Architecture



\### Services:

| Service | Port | Responsibility |

|---------|------|----------------|

| product-service | 5001 | Manages product catalog |

| order-service | 5002 | Handles order creation |



\### Communication:

\- order-service calls product-service via HTTP

\- Docker internal network enables service discovery by name



\## 3. Implementation



\### Technologies Used:

\- Python Flask for REST APIs

\- Docker for containerization

\- Docker Compose for orchestration



\### Key Features:

\- Health check endpoints

\- Environment variables for configuration

\- Timeout (2 seconds) and Retry logic (3 attempts)

\- Graceful error handling



\## 4. Results



\### Successful Scenarios:

\- Health checks return status "up"

\- Product lookup returns correct data

\- Order creation calculates total price correctly



\### Failure Scenario:

\- When product-service is stopped, order-service returns:

&#x20; `{"error": "product-service unavailable"}`

\- System recovers automatically when product-service restarts



\## 5. Failure Analysis



\### Observations:

1\. \*\*Failure Propagation\*\*: order-service depends on product-service

2\. \*\*Graceful Degradation\*\*: System returns meaningful error instead of crashing

3\. \*\*Self-Healing\*\*: Docker restart policy can auto-recover failed services



\### Resilience Mechanisms:

\- Timeout prevents infinite waiting

\- Retry handles temporary failures

\- Health checks enable monitoring



\## 6. 12-Factor App Principles Applied



| Principle | Implementation |

|-----------|----------------|

| III. Config | Environment variables |

| VI. Processes | Stateless services |

| VII. Port Binding | Each service binds to its port |

| XI. Logs | Docker manages logs |



\## 7. Conclusion



This lab demonstrated:

\- Benefits of microservices architecture

\- Importance of resilience patterns

\- Docker's role in cloud-native development

\- Trade-offs between monolith and microservices



\### Key Learnings:

\- Microservices enable independent deployment

\- Network failures must be handled explicitly

\- Health checks are essential for monitoring

\- Docker Compose simplifies multi-service orchestration

