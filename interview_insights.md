> ### "Can you walk me through an end-to-end project you've worked on?"
>
One project I worked on was an end-to-end sales analytics pipeline designed to simulate a real-world data analyst workflow.

The goal was to take raw sales data and turn it into analytics-ready tables that could be easily used for reporting and dashboards.

I used Databricks as the execution environment, SQL for staging and modeling, and PySpark for the transformation layer. Raw CSV files are ingested into a governed storage layer, staged using SQL tables, and then transformed with PySpark to create dimension tables like customers and products, as well as a fact table for sales.

The final output is a clean star-schema-style dataset that can be queried with SQL to answer business questions such as revenue trends, top customers, and product performance.

<br>
<br>

> ### “Why did you use PySpark for the transformations instead of doing everything in SQL?”
>
I used PySpark for the transformation layer because it scales well for large datasets and fits naturally into the Databricks ecosystem.

While many of the transformations could technically be done in SQL, PySpark allows me to handle more complex joins, calculations, and transformations in a way that’s easier to extend as data volume grows.

In smaller projects or simpler transformations, I’m comfortable using SQL end-to-end, but for this project I intentionally used PySpark to mirror how analytics pipelines are often built in larger organizations where Spark is the primary processing engine.

<br>
<br>

> ### “How do you ensure data quality in this pipeline?”
>
For data quality, I focus on a few key checks throughout the pipeline.

First, at the staging level, I rely on schema inference and basic validations to make sure columns have the expected data types and that critical fields like IDs are not null.

During the PySpark transformation step, I ensure joins behave as expected and that calculations like revenue are derived consistently from quantity and price.

Finally, after loading the analytics tables, I validate the results using SQL checks, such as row counts, null checks on key columns, and sanity checks on aggregated metrics like total revenue.

While this project keeps data quality lightweight, the structure allows additional checks or automated validations to be added as the pipeline scales.

<br>
<br>

> ### “If the data volume suddenly increased 10x, what changes would you make to this pipeline?”
>
If the data volume increased significantly, I would focus on both the Spark processing layer and the data model.

On the PySpark side, I would review joins and transformations to make sure they are efficient, and consider partitioning data on commonly filtered columns such as order date to improve performance.

I would also look into optimizing table storage by using partitioned tables and avoiding unnecessary columns in transformations.

From a querying perspective, I’d ensure that analytics tables are designed to support common access patterns, so that downstream SQL queries remain fast even as data volume grows.