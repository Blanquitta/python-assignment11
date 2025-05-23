# 2
import pandas as pd
import matplotlib.pyplot as plt
import sqlite3

# Connect to the database
conn = sqlite3.connect("../db/lesson.db")

# SQL query to get total revenue per order
query = """
SELECT o.order_id, 
       SUM(p.price * l.quantity) AS total_price
FROM orders o
JOIN line_items l ON o.order_id = l.order_id
JOIN products p ON l.product_id = p.product_id
GROUP BY o.order_id
ORDER BY o.order_id;
"""

# Load into DataFrame
df = pd.read_sql_query(query, conn)
conn.close()

# Optional: convert order_id to int and sort if necessary
df["order_id"] = df["order_id"].astype(int)
df = df.sort_values(by="order_id").reset_index(drop=True)

# Calculate cumulative revenue using cumsum (faster than apply)
df["cumulative"] = df["total_price"].cumsum()

# Plot cumulative revenue vs. order_id
plt.figure(figsize=(10, 6))
plt.plot(df["order_id"], df["cumulative"], marker='o', linestyle='-', color='darkblue')

# Add titles and labels
plt.title("Cumulative Revenue by Order ID")
plt.xlabel("Order ID")
plt.ylabel("Cumulative Revenue ($)")
plt.grid(True)
plt.tight_layout()

# Show the plot
plt.show()