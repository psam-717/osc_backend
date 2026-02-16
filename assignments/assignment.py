products = {
    "Ankara fabric": 120.50,
    "Plantain chips (pack)": 15.00,
    "Palm oil (1L)": 45.00,
    "Waakye (plate)": 25.00,
    "Fufu portion": 35.00
}

cart = ["Ankara fabric", "Plantain chips (pack)", "Palm oil (1L)", "Fufu portion", "Fufu portion", "Gobe"]

subtotal = 0
for cart_item in cart:
    if (cart_item in products):
        # store their prices
        item_price = products[cart_item]
        subtotal += item_price
        print(f"{cart_item:} : {item_price}")
    else:
        print(f"{cart_item} is not in products available")

print("\nSubtotal", subtotal)

# calculating discount
if subtotal > 200:
    discounted_price = 0.1 * subtotal
    subtotal -= discounted_price
elif subtotal > 100:
    discounted_price = 0.05 * subtotal
    subtotal -= discounted_price

print("discounted price", discounted_price)
print("total", subtotal)


