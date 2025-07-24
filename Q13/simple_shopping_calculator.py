items = []
num_items = 3

for i in range(1, num_items + 1):
    price = float(input(f"Enter price of item {i}: "))
    quantity = int(input(f"Enter quantity of item {i}: "))
    total = price * quantity
    items.append((price, quantity, total))

subtotal = sum(item[2] for item in items)
tax = round(subtotal * 0.085, 2)
total = round(subtotal + tax, 2)

print()

for i, (price, quantity, item_total) in enumerate(items, start=1):
    print(f"Item {i}: {price} x {quantity} = {item_total}")

print(f"Subtotal: {subtotal}")
print(f"Tax (8.5%): {tax}")
print(f"Total: {total}")
