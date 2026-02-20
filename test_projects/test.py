from pprint import pprint
from collections import Counter

cart_demo = ["Apple", "Mango", "Watermelon", "Watermelon", "Grape"]
products_demo = {
    "Apple": 20,
    "Mango": 35,
    "Watermelon": 40,
    "Pear": 50
}

# Count items in cart and identify unknown items
cart_count = Counter(cart_demo)
items_absent = [item for item in cart_count if item not in products_demo]

# Calculate cart items and total
cart_items = {}
total = 0
for item, qty in cart_count.items():
    if item in products_demo:
        price = products_demo[item]
        subtotal = qty * price
        total += subtotal
        cart_items[item] = {"quantity": qty, "price": price, "subtotal": subtotal}

# Build final result
all_items = {
    "items": cart_items,
    "total_items": len(cart_items),
    "subtotal": total,
    "has_unknown_items": bool(items_absent)
}

if items_absent:
    all_items["unknown_items"] = items_absent

pprint(all_items, width=100)
