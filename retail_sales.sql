-- 1. Create the table
CREATE TABLE retail_sales (
    order_id VARCHAR(50),
    order_date DATE,
    region VARCHAR(50),
    category VARCHAR(50),
    product_name VARCHAR(100),
    sales DECIMAL(10,2),
    quantity INT,
    profit DECIMAL(10,2)
);

-- 2. Load data (optional command, just a comment if you had trouble running it)
-- LOAD DATA LOCAL INFILE 'C:/retail_sales.csv'
-- INTO TABLE retail_sales
-- FIELDS TERMINATED BY ','
-- ENCLOSED BY '"'
-- LINES TERMINATED BY '\n'
-- IGNORE 1 ROWS;

-- 3. Sample queries

-- Total Sales
SELECT SUM(sales) AS total_sales FROM retail_sales;

-- Sales by Region
SELECT region, SUM(sales) AS sales FROM retail_sales GROUP BY region;

-- Sales and Profit by Category
SELECT category, SUM(sales) AS total_sales, SUM(profit) AS total_profit
FROM retail_sales
GROUP BY category;

-- Monthly Sales Trend
SELECT 
    DATE_FORMAT(order_date, '%Y-%m') AS month,
    SUM(sales) AS monthly_sales
FROM retail_sales
GROUP BY month
ORDER BY month;
