\# AWS Employee Management Web Application



<p align="center">

&#x20; \*\*Serverless Employee Management Application on AWS\*\*

</p>



A serverless web application built using AWS services to manage employee records with complete CRUD (Create, Read, Update, Delete) functionality.



The application uses Amazon S3 for frontend hosting, Amazon API Gateway for REST-style HTTP endpoints, AWS Lambda for backend processing, and Amazon DynamoDB for persistent data storage.



\---



\## Project Overview



This project demonstrates how to design and deploy a serverless web application using AWS managed services.



\### Key Features



\- Add new employee records

\- View all employees

\- Retrieve employee details by ID

\- Update employee information

\- Delete employee records

\- Web-based frontend interface

\- Serverless backend architecture

\- API integration with DynamoDB



\## Architecture



\*\*Application Request Flow:\*\*



User Browser → Amazon S3 → Amazon API Gateway → AWS Lambda → Amazon DynamoDB



\### AWS Services Used



| AWS Service | Purpose |

|---|---|

| Amazon S3 | Static website hosting |

| Amazon API Gateway | HTTP API and routing |

| AWS Lambda | Backend business logic |

| Amazon DynamoDB | Employee data storage |

| AWS IAM | Access control and permissions |

| Amazon CloudWatch | Lambda logs and monitoring |



See the `diagram/` directory for the architecture diagram.



\---



\## Technology Stack



| Technology | Usage |

|---|---|

| Python 3.12 | Backend development |

| Boto3 | AWS SDK for Python |

| HTML5 | Frontend structure |

| CSS3 | Frontend styling |

| JavaScript | API integration |

| JSON | API request and response |

| Postman | API testing |



\---



\## Project Directory Structure



```text

lambda-dynamodb/

│

├── backend/

│   ├── lambda\_function.py

│   └── requirements.txt

│

├── frontend\_page/

│   └── index.html

│

├── diagram/

│   └── architecture.png

│

├── Documents/

│   └── AWS\_Employee\_Management\_Project\_Guide.pdf

│

├── README.md

└── .gitignore

```



\---



\## AWS Infrastructure Configuration



\*\*AWS Region:\*\* `ap-southeast-2`



\### 1. Amazon DynamoDB



\- Table Name: `EmployeeTable`

\- Partition Key: `employeeId`

\- Key Type: String



Employee attributes:



| Attribute | Type |

|---|---|

| employeeId | String |

| employeeName | String |

| department | String |

| salary | Number |



\### 2. AWS Lambda



\- Function Name: `EmployeeManagementFunction`

\- Runtime: Python 3.12

\- Execution Role: `Lambda-EmployeeApp-ExecutionRole`

\- AWS SDK: Boto3



The Lambda function handles API requests and performs database operations using DynamoDB.



\### 3. Amazon API Gateway



\- API Name: `EmployeeManagementAPI`

\- API Type: HTTP API

\- API ID: `jndh8i2d68`

\- Stage: `$default`

\- Payload Format: 2.0



\### API Endpoints



| HTTP Method | Endpoint | Description |

|---|---|---|

| POST | `/employees` | Create employee |

| GET | `/employees` | Retrieve all employees |

| GET | `/employees/{employeeId}` | Retrieve employee by ID |

| PUT | `/employees/{employeeId}` | Update employee |

| DELETE | `/employees/{employeeId}` | Delete employee |



API Base URL:



```text

https://jndh8i2d68.execute-api.ap-southeast-2.amazonaws.com

```



\### 4. Amazon S3



S3 is used to host the static frontend website.



Configuration:

\- Static Website Hosting: Enabled

\- Index Document: `index.html`

\- Frontend: HTML, CSS and JavaScript



\### 5. IAM Permissions



Lambda execution role has the following permissions:



\- `AWSLambdaBasicExecutionRole`

\- `dynamodb:PutItem`

\- `dynamodb:GetItem`

\- `dynamodb:Scan`

\- `dynamodb:UpdateItem`

\- `dynamodb:DeleteItem`



DynamoDB permissions are scoped to the EmployeeTable resource.



\---



\## Application Screenshots



Add your project screenshots to the `Documents/` or a dedicated `screenshots/` directory.



Suggested screenshots:



1\. Employee Management frontend

2\. DynamoDB EmployeeTable

3\. Lambda function

4\. API Gateway routes

5\. Postman CRUD testing

6\. S3 static website hosting



\---



\## Project Implementation Steps



1\. Created DynamoDB EmployeeTable.

2\. Created IAM execution role and DynamoDB access policy.

3\. Created Python Lambda function.

4\. Integrated Lambda with DynamoDB using Boto3.

5\. Implemented employee CRUD operations.

6\. Created API Gateway HTTP API.

7\. Configured five API routes.

8\. Tested APIs using Postman.

9\. Created S3 bucket.

10\. Enabled static website hosting.

11\. Uploaded frontend `index.html`.

12\. Configured API Gateway CORS.

13\. Integrated frontend with API Gateway.

14\. Verified end-to-end CRUD operations.



\---



\## Testing and Validation



All CRUD operations were tested successfully.



| Test Case | Result |

|---|---|

| Create Employee | Successful |

| List Employees | Successful |

| Get Employee by ID | Successful |

| Update Employee | Successful |

| Delete Employee | Successful |

| Frontend API Integration | Successful |

| DynamoDB Data Persistence | Verified |



\---



\## Security Considerations



This is a hands-on learning project. Before production deployment, consider:



\- Keeping the S3 bucket private and using CloudFront with Origin Access Control.

\- Implementing authentication and authorization.

\- Restricting CORS to the frontend domain.

\- Applying input validation.

\- Enabling CloudWatch monitoring and alarms.

\- Avoiding hardcoded credentials and secrets.

\- Implementing appropriate API throttling.



\---



\## Future Improvements



\- CloudFront CDN integration

\- Amazon Cognito authentication

\- CloudWatch dashboards and alarms

\- Terraform infrastructure automation

\- GitHub Actions CI/CD pipeline

\- Automated deployment and rollback



\---



\## Author



\*\*Barun Mondal\*\*



Cloud | DevOps | Site Reliability Engineering (SRE)



\---



\## Project Status



\*\*Completed – End-to-End CRUD Operations Verified\*\*



Built and tested using AWS serverless services.

