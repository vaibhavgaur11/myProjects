Employee Management API

A secure ASP.NET Core Web API implementing CRUD operations with SQL Server, API Key authentication, and IIS hosting.

Tech Stack

ASP.NET Core Web API

Entity Framework Core

SQL Server

API Key Authentication (Custom Middleware)

Swagger / OpenAPI

IIS Hosting

 Architecture Overview
Client (Swagger/Postman/Browser)
        │
        ▼
IIS (Hosting Layer)
        │
        ▼
ASP.NET Core API
        │
        ▼
API Key Middleware (Security Layer)
        │
        ▼
Controller Layer
        │
        ▼
Entity Framework Core
        │
        ▼
SQL Server (CompanyDB)

Authentication

This API uses a custom middleware based API Key authentication mechanism.

All requests must include the following header:

X-API-KEY: your-secret-key


Requests without a valid API key will return:

401 Unauthorized

Endpoints
Get All Employees
GET /api/EmployeeAPI

Get Employee By ID
GET /api/EmployeeAPI/{id}

Create Employee
POST /api/EmployeeAPI


Request Body:

{
  "name": "Riya",
  "designation": "Analyst"
}



Setup Instructions (Local Development)

Clone the repository

git clone <your-repo-url>


Update appsettings.json with your SQL Server connection string:

"ConnectionStrings": {
  "DefaultConnection": "Server=YOUR_SERVER;Database=CompanyDB;Trusted_Connection=True;TrustServerCertificate=True;"
}


Apply migrations (if using migrations)

dotnet ef database update


Run the application

dotnet run


Open Swagger:

https://localhost:<port>/swagger

Hosting

The API is deployed and tested on IIS.
Successfully accessed from another machine over the local network.

📌 Key Learnings

Implementing custom API Key authentication

Integrating EF Core with SQL Server

Secure API configuration with Swagger

IIS deployment and external access testing

Understanding full request lifecycle

🔮 Future Improvements

JWT Authentication

Role Based Authorization

Global Exception Handling

Logging with Serilog

Docker Deployment

Azure Hosting

📎 License

This project is for learning and demonstration purposes.