EmployeeAPI – Azure SQL Migration Project

Table of Contents

Project Overview Tech Stack Architecture Local Setup Azure Resource
Creation Database Migration Process API Configuration Update Testing via
Swagger Security Configuration Screenshots (Proof of Deployment) Cleanup

1.  Project Overview

This project demonstrates migrating a local SQL Server database to Azure
SQL Database and updating a .NET Web API to use the cloud database.

The API performs CRUD operations on Employee data and is secured using
an API Key middleware.

2.  Tech Stack

.NET Web API Entity Framework Core SQL Server (Local) Azure SQL Database
(Basic Tier) SQL Server Management Studio (SSMS) Swagger (Swashbuckle)

3.  Architecture

Local API → Azure SQL Database Authentication → SQL Authentication API
Security → Custom API Key Middleware

4.  Local Setup

Clone repository Configure local SQL Server Update appsettings.json with
local connection string Run migrations (if applicable) Run API and
verify via Swagger

5.  Azure Resource Creation

5.1 Create Resource Group

Name: migrateSQL Region: Central India

[Add Screenshot – Azure Resource Group]

5.2 Create Azure SQL Logical Server

Server Name: vibhuuu Authentication: SQL Authentication Firewall: Client
IPv4 added

[Add Screenshot – Azure SQL Logical Server Overview]

5.3 Create Azure SQL Database

Database Name: employeapi Pricing Tier: Basic Backup: Locally Redundant

[Add Screenshot – Azure SQL Database Configuration]

6.  Database Migration Process

6.1 Export Local Database

SSMS → Right Click DB Tasks → Export Data-tier Application Generated
.bacpac

[Add Screenshot – SSMS Export Wizard]

6.2 Import to Azure SQL

Connect to Azure SQL via SSMS Import Data-tier Application Target
Database: employeapi

[Add Screenshot – SSMS Import Progress]

6.3 Verification

Executed:

SELECT DB_NAME(); SELECT * FROM INFORMATION_SCHEMA.TABLES;

Confirmed Employees table exists.

[Add Screenshot – Azure SQL Tables in SSMS]

7.  API Configuration Update

Updated appsettings.json:

“ConnectionStrings”: { “DefaultConnection”:
“Server=tcp:vibhuuu.database.windows.net,1433;Initial
Catalog=employeapi;User ID=XXXX;Password=XXXX;Encrypt=True;” }

Restarted API. Verified successful connection.

8.  Testing via Swagger

Endpoints Tested:

GET /api/EmployeeAPI GET /api/EmployeeAPI/{id} POST /api/EmployeeAPI PUT
/api/EmployeeAPI/{id} DELETE /api/EmployeeAPI/{id}

All operations validated against Azure SQL.

[Add Screenshot – Swagger GET Success Response] [Add Screenshot –
Swagger POST Success Response]

9.  Security Configuration

SQL Authentication enabled Azure Firewall rule configured for client
IPv4 API Key middleware enforced via X-API-KEY header

Example Header:

X-API-KEY: SuperSecretKey123

10. Screenshots (Proof of Deployment)

Add the following:

Azure Resource Group Azure SQL Logical Server Azure SQL Database
Overview Firewall Configuration SSMS Connected to Azure SQL Tables in
Azure Database Swagger Successful API Calls

11. Cleanup

To avoid unnecessary charges:

Delete Resource Group migrateSQL Confirm all resources are removed
