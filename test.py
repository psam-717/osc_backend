from pprint import pprint

cart_demo = ["Apple", "Mango", "Watermelon", "Watermelon", "Grape"]
products_demo = {
    "Apple": 20,
    "Mango": 35,
    "Watermelon": 40,
    "Pear": 50
}


# keep count and list of items available in products
# keep count and list of items not in products
# calculate subtotal


count = {}
items_present = []
items_absent = []


for item in cart_demo:
    if item in products_demo:
        if item in count:
            count[item] += 1
        else:
            count[item] = 1
        # items_present.append(item)
    else:
        items_absent.append(item)

all_items = {}
cart_items = {}
total = 0
for item, qty in count.items():
    price = products_demo[item]
    subtotal = qty * price
    total += subtotal
    
    cart_items[item] ={"quantity": qty, "price": price, "subtotal": subtotal}
    all_items["items"] = cart_items
    all_items["total_items"] = len(count)
    all_items["subtotal"] = total
    if len(items_absent) > 0:
        all_items["unknown_items"] = items_absent
        all_items["has_unknown_items"] = True
    else:
        all_items["has_unknown_items"] = False
    
pprint(all_items, width=100)
