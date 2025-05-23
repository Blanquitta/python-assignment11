# Task 1
import pandas as pd
import matplotlib.pyplot as plt
# import sqlite3
# data = {
#     "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
#     "Sales": [100, 150, 200, 250, 300, 350],
#     "Expenses": [80, 120, 180, 200, 220, 300]
# }
# df = pd.DataFrame(data)

# # Line Plot
# df.plot(x="Month", y=["Sales", "Expenses"], kind="line", title="Sales vs. Expenses")
# plt.show()

# # Bar Plot
# df.plot(x="Month", y="Sales", kind="bar", color="skyblue", title="Monthly Sales")
# plt.show()




# Connect to the database
conn = sqlite3.connect("../db/lesson.db")

# SQL query to calculate revenue per employee
query = """
SELECT last_name, 
       SUM(price * quantity) AS revenue 
FROM employees e 
JOIN orders o ON e.employee_id = o.employee_id 
JOIN line_items l ON o.order_id = l.order_id 
JOIN products p ON l.product_id = p.product_id 
GROUP BY e.employee_id;
"""

# Load into a DataFrame
employee_results = pd.read_sql_query(query, conn)

# Close the connection
conn.close()

employee_results = employee_results.sort_values(by="revenue", ascending=False)

# Plot
plt.figure(figsize=(10, 6))
employee_results.plot(kind='bar', x='last_name', y='revenue', color='teal', legend=False)

# Titles and labels
plt.title("Revenue by Employee")
plt.xlabel("Employee Last Name")
plt.ylabel("Total Revenue ($)")
plt.xticks(rotation=45)
plt.tight_layout()

# Show plot
plt.show()

# Task 3

import plotly.express as px
import plotly.data as pldata
df = pldata.wind(return_type='pandas')

print("First 10 rows:")
print(df.head(10))

print("\nLast 10 rows:")
print(df.tail(10))

# Clean the 'strength' column: remove '+' and convert to float
df['strength'] = df['strength'].str.replace('+', '', regex=False).astype(float)

# Create interactive scatter plot
fig = px.scatter(
    df,
    x='strength',
    y='frequency',
    color='direction',
    title='Wind Strength vs Frequency by Direction',
    labels={'strength': 'Wind Strength', 'frequency': 'Frequency'},
    template='plotly_dark'
)

# Save the plot to an HTML file
fig.write_html("wind.html")

# To verify in Jupyter/Notebook environment, show the figure:
fig.show()
