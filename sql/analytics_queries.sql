-- ============================================
-- Revenue by day
-- ============================================
SELECT
    order_date,
    SUM(revenue) AS total_revenue
FROM fact_sales
GROUP BY order_date
ORDER BY order_date;


-- ============================================
-- Revenue by product category
-- ============================================
SELECT
    p.category,
    SUM(f.revenue) AS total_revenue
FROM fact_sales f
JOIN dim_products p
    ON f.product_id = p.product_id
GROUP BY p.category
ORDER BY total_revenue DESC;


-- ============================================
-- Top customers by total spend
-- ============================================
SELECT
    c.customer_id,
    c.first_name,
    c.last_name,
    SUM(f.revenue) AS total_spent
FROM fact_sales f
JOIN dim_customers c
    ON f.customer_id = c.customer_id
GROUP BY
    c.customer_id,
    c.first_name,
    c.last_name
ORDER BY total_spent DESC
LIMIT 10;


-- ============================================
-- Average order value
-- ============================================
SELECT
    ROUND(SUM(revenue) / COUNT(DISTINCT order_id), 2) AS avg_order_value
FROM fact_sales;