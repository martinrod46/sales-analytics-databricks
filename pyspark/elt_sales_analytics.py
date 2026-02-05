from pyspark.sql import SparkSession
from pyspark.sql.functions import col, round as spark_round

# -----------------------------------
# Spark session
# -----------------------------------
spark = SparkSession.builder.appName("SalesAnalyticsETL").getOrCreate()

# -----------------------------------
# Read staging tables (Unity Catalog)
# -----------------------------------
customers = spark.table("customers_staging")
products = spark.table("products_staging")
orders = spark.table("orders_staging")
order_items = spark.table("order_items_staging")

# -----------------------------------
# Dimension: Customers
# -----------------------------------
dim_customers = (
    customers
    .select(
        "customer_id",
        "first_name",
        "last_name",
        "email",
        "country"
    )
)

# -----------------------------------
# Dimension: Products
# -----------------------------------
dim_products = (
    products
    .select(
        "product_id",
        "product_name",
        "category",
        "price"
    )
)

# -----------------------------------
# Fact: Sales
# -----------------------------------
fact_sales = (
    orders
    .join(order_items, "order_id")
    .join(products, "product_id")
    .select(
        orders.order_id,
        orders.order_date,
        orders.customer_id,
        products.product_id,
        order_items.quantity,
        products.price,
        spark_round(order_items.quantity * products.price, 2).alias("revenue")
    )
)

# -----------------------------------
# Write analytics tables
# -----------------------------------
dim_customers.write.mode("overwrite").saveAsTable("dim_customers")
dim_products.write.mode("overwrite").saveAsTable("dim_products")
fact_sales.write.mode("overwrite").saveAsTable("fact_sales")

print("ETL completed successfully")

spark.stop()