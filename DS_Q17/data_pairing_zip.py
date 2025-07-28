products = ["Laptop", "Mouse", "Keyboard", "Monitor"]
prices = [999.99, 25.50, 75.00, 299.99]
quantities = [5, 20, 15, 8]

# 1. Create Product-Price Pairs
product_price_pairs = list(zip(products, prices))
print("Product-Price Pairs:")
for product, price in product_price_pairs:
    print(f"{product}: ${price}")

# 2. Calculate Total Value for Each Product
print("\nTotal Inventory Value:")
for product, price, quantity in zip(products, prices, quantities):
    total_value = price * quantity
    print(f"{product}: ${total_value:.2f}")

# 3. Build a Product Catalog Dictionary
product_catalog = {
    product: {"price": price, "quantity": quantity}
    for product, price, quantity in zip(products, prices, quantities)
}
print("\nProduct Catalog:")
for product, details in product_catalog.items():
    print(f"{product}: {details}")

# 4. Find Low Stock Products (quantity < 10)
low_stock = [product for product, quantity in zip(products, quantities) if quantity < 10]
print("\nLow Stock Products:")
for product in low_stock:
    print(product)
