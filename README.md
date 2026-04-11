# Data Warehouse and Analytics Project 🚀

Welcome to the **Data Warehouse and Analytics Project** repository! 
This project demonstrates a comprehensive data warehousing and analytics solution using Python and SQL, covering everything from raw data ingestion to generating actionable business insights.

---

## 📖 Project Overview
This project involves building a modern data warehouse using the **Medallion Architecture** (Bronze, Silver, and Gold layers).

1. **Data Architecture**: Designing a 3-tier warehouse for structured data.
2. **ETL Pipelines**: Extracting, transforming, and loading data from ERP and CRM systems.
3. **Data Modeling**: Developing Fact and Dimension tables (Star Schema).
4. **Analytics & Reporting**: Validating data integrity and preparing it for BI tools.

---

## 🏗️ Data Architecture
The data flows through three main stages as shown in the diagram below:

![Data Architecture Diagram](docs/data_architecture.png) 


1. **Bronze Layer**: Stores raw data as-is from source systems (CSV files).
2. **Silver Layer**: Performs data cleansing, standardization, and handling missing values.
3. **Gold Layer**: Houses business-ready data modeled into a **Star Schema** for reporting.

---

## 🛠️ Tools & Technologies
- **Language**: Python (Pandas, SQLAlchemy)
- **Database**: SQL Server (or PostgreSQL/SQLite)
- **Environment**: Jupyter Notebooks / Python Scripts
- **Documentation**: Draw.io (for diagrams)
- **Version Control**: Git & GitHub

---

## 📂 Repository Structure
```text
data-warehouse-project/
│
├── datasets/                           # Raw datasets (ERP and CRM CSV files)
│
├── docs/                               # Project documentation and architecture details
│   ├── data_architecture.png           # Architecture diagram (Medallion Layers)
│   ├── data_catalog.md                 # Metadata and field descriptions
│   └── naming_conventions.md           # Naming guidelines for variables and tables
│
├── scripts/                            # Python ETL Pipeline
│   ├── load_bronze.py                  # Script for raw data ingestion to SQL
│   ├── load_silver.py                  # Script for data cleaning & transformation
│   └── load_gold.py                    # Script for Star Schema modeling (Facts & Dims)
│
├── tests/                              # Data Quality & Validation scripts
│   └── quality_checks.py               # Python tests for nulls, duplicates & integrity
│
├── README.md                           # Project overview and instructions
├── LICENSE                             # MIT License information
└── requirements.txt                    # Python dependencies (Pandas, SQLAlchemy, etc.)
```

---
## 🛡️ License
This project is licensed under the [MIT License](LICENSE). You are free to use, modify, and share this project with proper attribution.

---

## About Me
Hi there! I'm **[Abdulrahman Ayman Farag]**, a Data Engineer/Analyst passionate about turning raw data into meaningful stories. 
Feel free to connect with me on [[LinkedIn](https://www.linkedin.com/in/abdelrhman-ayman-45b854361?utm_source=share_via&utm_content=profile&utm_medium=member_android)] or check my other projects!
