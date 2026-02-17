EmployeeAPI – Azure SQL Migration Project

Table of Contents

1.Project Overview 
2.Tech Stack 
3.Architecture 
4.Local Setup 
5.Azure Resource Creation 6.Database Migration Process 
7.API Configuration 
8.Update Testing via Swagger 
9.Security Configuration 
10.Screenshots (Proof of Deployment) 
11.Cleanup

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
<img width="1742" height="536" alt="image" src="https://github.com/user-attachments/assets/22442694-f378-4a26-8940-9ce5f3b44183" />


4.  Local Setup

Clone repository Configure local SQL Server Update appsettings.json with
local connection string Run migrations (if applicable) Run API and
verify via Swagger

5.  Azure Resource Creation

5.1 Create Resource Group

Name: migrateSQL Region: Central India

[Screenshot – Azure Resource Group]
<img width="1837" height="648" alt="image" src="https://github.com/user-attachments/assets/7b3c909e-468c-46ed-b419-02c7ab765589" />


5.2 Create Azure SQL Logical Server

Server Name: vibhuuu Authentication: SQL Authentication Firewall: Client
IPv4 added

[Screenshot – Azure SQL Logical Server Overview]
<img width="1838" height="752" alt="image" src="https://github.com/user-attachments/assets/bdd7ae28-790a-49e7-b55b-7f683794581e" />


5.3 Create Azure SQL Database

Database Name: employeapi Pricing Tier: Basic Backup: Locally Redundant

[Screenshot – Azure SQL Database Configuration]
<img width="1840" height="873" alt="image" src="https://github.com/user-attachments/assets/4d803d66-d746-46c5-a2ec-3543f99b4ca7" />


6.  Database Migration Process

6.1 Export Local Database

SSMS → DB Tasks → Exported Data-tier Application Generated
.bacpac


6.2 Import to Azure SQL

Connected to Azure SQL via SSMS Import Data-tier Application Target
Database: employeapi

<img width="1918" height="980" alt="image" src="https://github.com/user-attachments/assets/14be4d58-3797-4976-a025-545d87589224" />


6.3 Verification

Executed:

SELECT TOP (1000) [EmployeeId]
      ,[Name]
      ,[Designation]
  FROM [dbo].[Employees]

Confirmed Employees table exists.


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

[Screenshot – Swagger GET Success Response]
<img width="1405" height="906" alt="image" src="https://github.com/user-attachments/assets/2783b644-15ad-4c61-ae2e-b8136638eed3" />


[ Screenshot – Swagger POST Success Response]
<img width="1052" height="901" alt="image" src="https://github.com/user-attachments/assets/a5312651-0189-4df2-833b-5cd404264d61" />


9.  Security Configuration

SQL Authentication enabled Azure Firewall rule configured for client
IPv4 API Key middleware enforced via X-API-KEY header

Example Header:

X-API-KEY: SuperSecretKey123

10. Screenshots (Proof of Deployment)

Add the following:
<img width="1837" height="649" alt="image" src="https://github.com/user-attachments/assets/1c9b30dd-a2c5-41f5-858b-e8a7aaf83a4b" />
<img width="1837" height="648" alt="image" src="https://github.com/user-attachments/assets/918893fb-ba66-49a4-b0ca-f7d0fa724f6c" />
<img width="1838" height="752" alt="image" src="https://github.com/user-attachments/assets/a7a7df51-250c-4a79-bf94-32f45eaa463f" />

<img width="1840" height="873" alt="image" src="https://github.com/user-attachments/assets/e9b6e874-6423-4649-931c-f88b945ea3d7" />
<img width="1919" height="980" alt="image" src="https://github.com/user-attachments/assets/ab1c02d6-e770-452f-a891-24a607b345eb" />
<img width="1918" height="980" alt="image" src="https://github.com/user-attachments/assets/ac3f1b3a-416b-48ee-ae6c-4e166fd7ff4e" />

<img width="1405" height="906" alt="image" src="https://github.com/user-attachments/assets/3e6bc258-7c4d-400e-af14-ac78f79148dd" />
<img width="1057" height="911" alt="image" src="https://github.com/user-attachments/assets/a22917ec-5494-45f1-a1db-a6ee658d5a07" />



11. Cleanup

To avoid unnecessary charges:

Delete Resource Group migrateSQL Confirm all resources are removed
