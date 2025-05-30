# Serverless REST API with DynamoDB and API Gateway
## 📌 Project Overview
This project demonstrates a serverless REST API built using AWS services to manage a simple To-Do list or Customer Records. The API supports full CRUD operations and is designed with scalability, cost-efficiency, and maintainability in mind.

### 🧱 Architecture
Architecture Type: Serverless

### Core AWS Services:

- Amazon API Gateway – Exposes HTTP RESTful endpoints

- AWS Lambda – Executes backend logic for API requests

- Amazon DynamoDB – Stores data in a NoSQL format

- AWS IAM – Manages access control for AWS resources

- Amazon CloudWatch – Provides logging and monitoring

### Architecture
![AWS Architecture](https://github.com/user-attachments/assets/031997a5-93d9-454b-a8cc-62494c160a64)



### ✨ Features
- Create, Read, Update, Delete (CRUD) operations on records

- Stateless, event-driven backend logic using AWS Lambda

- Fast and scalable data access using DynamoDB

- Secure access control using IAM roles and resource policies

- CloudWatch integration for logging and metrics

### 📚 Learning Outcomes
- Understand serverless architecture design

- Deploy APIs using API Gateway and Lambda

- Use DynamoDB efficiently with best practices (partition keys, capacity modes, etc.)

- Apply IAM roles and policies to secure your application

- Monitor and debug serverless applications using CloudWatch

### 🚀 Getting Started
#### Prerequisites:
- AWS Account

- AWS CLI configured

- Node.js or Python (based on your Lambda functions)

- Serverless Framework

#### Deployment Steps:
- Clone the repository
 ``` bash
- git clone https://github.com/Dalia-Karam/AWS-SSA-Project.git
- cd AWS-SSA-Project
```
- Set environment variables or config files if needed

- Deploy infrastructure using your preferred method (e.g., Serverless Framework, AWS Console)

- Test API endpoints using Postman or curl
### 🧪 API Endpoints
- POST /operations – Create a new item

- GET /operations – Retrieve all items

- GET /operations/{id} – Retrieve an item by ID

- POST /operations/{id} – Update an item

- DELETE /operations/{id} – Delete an item

### 🔐 Security
- IAM roles defined with least privilege principle

- API Gateway resource policies for controlling access

- CloudWatch for monitoring suspicious behavior

### 📊 Monitoring & Logging
- Lambda logs accessible via CloudWatch Logs

- API metrics (latency, errors) available in CloudWatch Metrics

### 🛠️ Tools Used
- AWS Lambda

- Amazon API Gateway

- Amazon DynamoDB

- IAM

- CloudWatch

