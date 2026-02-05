# 📊 Sales Analytics Pipeline (Databricks + PySpark + SQL)

### 🚀 Project Overview

This project is an end-to-end sales analytics pipeline designed to simulate a real-world data analyst / analytics engineer workflow using Databricks, PySpark, and SQL.

The pipeline ingests raw CSV sales data, stages it using SQL, transforms it with PySpark, and produces analytics-ready dimension and fact tables that can be queried for business insights.

The goal of this project is to demonstrate:

- Data modeling 
- ETL / ELT concepts 
- SQL analytics 
- PySpark transformations 
- Git-based workflow 
- Databricks + Unity Catalog best practices


<br>
<br>


### 🧱 Architecture

Raw CSV Files \
   ↓ \
Unity Catalog Volume (raw_sales_data) \
   ↓ \
Staging Tables (SQL) \
   ↓ \
PySpark ETL \
   ↓ \
Analytics Tables (dim & fact) \
   ↓ \
Business Analytics (SQL queries) 

<br>
<br>

### 🛠️ Tech Stack

- Databricks -> Execution environment 
- Apache Spark (PySpark) -> ETL transformations 
- SQL -> Staging, modeling and analytics 
- Unity Catalog -> Data governance and storage 
- GitHub -> Version control

<br>
<br>

### 📁 Repository Structure

sales_analytics_pipeline/ \
├── pyspark/ \
│   └── etl_sales_analytics.py \
│ \
├── sql/ \
│   └── analytics_queries.sql \
│ \
└── README.md 

<br>
<br>

### 📥 Data Ingestion

Raw data is stored as CSV files in a Unity Catalog Volume.

Files include: 

- Customers 
- Products 
- Orders 
- Order_items 

**Data is loaded into staging tables using SQL.**

<br>
<br>

### 🔄 ETL Process (PySpark)

The PySpark ETL script performs the following:

Dimensions:

- dim_customers 
- dim_products 

Fact Table:

- fact_sales

joins: 
- orders 
- order_items
- products

calculates revenue per line item

<br>
<br>

### 📊 Analytics & Business Queries

The SQL layer answers common business questions such as:

- Revenue by day 
- Revenue by product category 
- Top customers by spend 
- Average order value 


 These queries are stored in:

>> ### sql/analytics_queries.sql

<br>
<br>

### ▶️ How to Run

- Upload raw CSV files to a Unity Catalog volume. 
- Create staging tables using SQL. 
- Query analytics tables using SQL.

 Run the PySpark ETL script:

 >> ### pyspark/etl_sales_analytics.py



<br>
<br>

### 📌 Notes

- Raw data is not stored in GitHub. 
- All processing is done inside Databricks. 
- Project follows industry-standard analytics workflows.

<br>
<br>

### 👤 Author

Built as a hands-on learning project to practice real-world data analytics and engineering skills.

<br>
<br>

### 💼 Job Interview Insights

Built an interview-proof guide that can help in case you need to talk through this project confidently.

>> ### interview_insights.md document 