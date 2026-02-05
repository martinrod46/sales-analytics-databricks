# 📊 Sales Analytics Pipeline (Databricks + PySpark + SQL)

#### 🚀 Project Overview

This project is an end-to-end sales analytics pipeline designed to simulate a real-world data analyst / analytics engineer workflow using Databricks, PySpark, and SQL.

The pipeline ingests raw CSV sales data, stages it using SQL, transforms it with PySpark, and produces analytics-ready dimension and fact tables that can be queried for business insights.

The goal of this project is to demonstrate:

data modeling

ETL / ELT concepts

SQL analytics

PySpark transformations

Git-based workflow

Databricks + Unity Catalog best practices


🧱 Architecture
Raw CSV Files
   ↓
Unity Catalog Volume (raw_sales_data)
   ↓
Staging Tables (SQL)
   ↓
PySpark ETL
   ↓
Analytics Tables (dim & fact)
   ↓
Business Analytics (SQL queries)


🛠️ Tech Stack

Databricks – execution environment

Apache Spark (PySpark) – ETL transformations

SQL – staging, modeling, and analytics

Unity Catalog – data governance and storage

GitHub – version control


📁 Repository Structure
sales_analytics_pipeline/
├── pyspark/
│   └── etl_sales_analytics.py
│
├── sql/
│   └── analytics_queries.sql
│
└── README.md


📥 Data Ingestion

Raw data is stored as CSV files in a Unity Catalog Volume

Files include:

customers

products

orders

order_items

Data is loaded into staging tables using SQL


🔄 ETL Process (PySpark)

The PySpark ETL script performs the following:

Dimensions

dim_customers

dim_products

Fact Table

fact_sales

joins orders, order_items, and products

calculates revenue per line item



📊 Analytics & Business Queries

The SQL layer answers common business questions such as:

revenue by day

revenue by product category

top customers by spend

average order value

These queries are stored in:

sql/analytics_queries.sql


▶️ How to Run

Upload raw CSV files to a Unity Catalog volume

Create staging tables using SQL

Run the PySpark ETL script:

pyspark/etl_sales_analytics.py

Query analytics tables using SQL


📌 Notes

Raw data is not stored in GitHub

All processing is done inside Databricks

Project follows industry-standard analytics workflows.


👤 Author

Built as a hands-on learning project to practice real-world data analytics and engineering skills.