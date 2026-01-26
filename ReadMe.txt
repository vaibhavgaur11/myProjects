# Expense Tracker – ASP.NET Core MVC

A simple **Expense Tracker** application built using **ASP.NET Core (.NET 8)** and **SQLite**.  
This project is intended to demonstrate backend fundamentals, MVC architecture, database usage, and cloud-ready design.

---

## 🚀 Features

- Add and view expenses
- ASP.NET Core MVC with Razor views
- Entity Framework Core
- SQLite database (file-based)
- Clean separation of concerns
- Cloud & Docker ready (documented)

---

## 🛠 Tech Stack

- .NET 8
- ASP.NET Core MVC
- Entity Framework Core
- SQLite
- Visual Studio 2022
- Docker (explored)
- Azure (deployment documented)

---

## ▶️ Run Locally

### Prerequisites
- .NET 8 SDK
- Visual Studio 2022 or later

### Steps
```bash
dotnet run
Open in browser:

arduino
Copy code
http://localhost:8080/Expenses
🗃 Database
Uses SQLite

Database file is created automatically on first run

No manual setup required
E:\ExpenseTracker\ExpenseTracker\ExpenseTracker.csproj
Database file is excluded from Git using .gitignore

🐳 Docker (Optional)
This project was tested with Docker locally.
To use docker uncomment the Dockerfile and build the image in Program.cs

Typical flow:

bash
Copy code
docker build -t expense-tracker .
docker run -p 8080:8080 expense-tracker
Application URL:


Copy code
http://localhost:8080/Expenses
Dockerfile is intentionally not included in the current commit to keep the repository simple.

The Docker and cloud steps are documented below.

☁️ Azure Deployment (Documented)
This application is designed to be deployed as a container on Azure.

Planned Azure Resources
Resource Group

Azure Container Registry (ACR)

Azure Container Apps

Deployment Flow
Build Docker image

Push image to Azure Container Registry

Deploy image to Azure Container Apps

Access the app via public URL

Deployment can be done using:

Azure CLI

OR Visual Studio Publish (with Dockerfile)

🔁 CI/CD (Planned)
Future improvement:

Azure DevOps pipeline

Restore, build, and test

Docker image build

Push to ACR

Deploy to Azure Container Apps

📌 Notes
The project focuses on clarity and fundamentals

Cloud deployment steps are documented but not fully automated

Designed as a learning and portfolio project

👤 Author
Vaibhav Gaur

GitHub: https://github.com/vaibhavgaur11

