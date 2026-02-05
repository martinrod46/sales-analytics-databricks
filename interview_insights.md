> **"Can you walk me through an end-to-end project you've worked on?"**
>
One project I worked on was an end-to-end sales analytics pipeline designed to simulate a real-world data analyst workflow.

The goal was to take raw sales data and turn it into analytics-ready tables that could be easily used for reporting and dashboards.

I used Databricks as the execution environment, SQL for staging and modeling, and PySpark for the transformation layer. Raw CSV files are ingested into a governed storage layer, staged using SQL tables, and then transformed with PySpark to create dimension tables like customers and products, as well as a fact table for sales.

The final output is a clean star-schema-style dataset that can be queried with SQL to answer business questions such as revenue trends, top customers, and product performance.