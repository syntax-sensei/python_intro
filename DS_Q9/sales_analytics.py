sales_data = [
("Q1", [("Jan", 1000), ("Feb", 1200), ("Mar", 1100)]),
("Q2", [("Apr", 1300), ("May", 1250), ("Jun", 1400)]),
("Q3", [("Jul", 1350), ("Aug", 1450), ("Sep", 1300)])
]

# Task 1: Calculate Total Sales per Quarter using unpacking
print("=== Total Sales per Quarter ===")
for quarter_name, monthly_sales in sales_data:
    quarter_total = sum(sales for month, sales in monthly_sales)
    print(f"{quarter_name}: {quarter_total}")

# Overall total sales using unpacking
total_sales = sum(sales for quarter_name, monthly_sales in sales_data 
                 for month, sales in monthly_sales)
print(f"\nTotal sales across all quarters: {total_sales}")

# Task 2: Find the Month with Highest Sales using unpacking

month_with_highest_sales = max(
    ((month, sales) for quarter_name, monthly_sales in sales_data 
     for month, sales in monthly_sales),
    key=lambda x: x[1]
)
print(f"Verification using max(): {month_with_highest_sales}")

# Task 3: Create a Flat List of Monthly Sales using unpacking
print("\n=== Flat List of Monthly Sales ===")
flat_list_monthly_sales = [
    (month, sales) for quarter_name, monthly_sales in sales_data 
    for month, sales in monthly_sales
]
print("Flat list format (month, sales):", flat_list_monthly_sales)

# Task 4: Demonstrate Unpacking in Loops
print("\n=== Detailed Sales Report using Tuple Unpacking ===")
for quarter_name, monthly_sales in sales_data:
    print(f"\n{quarter_name} Sales:")
    for month, sales in monthly_sales:
        print(f"  {month}: ${sales:,}")
    
    # Calculate quarter total using unpacking
    quarter_total = sum(sales for month, sales in monthly_sales)
    print(f"  {quarter_name} Total: ${quarter_total:,}")

