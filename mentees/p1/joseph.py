products = {
    "Ankara fabric": 120.50,
    "Plantain chips (pack)": 15.00,
    "Palm oil (1L)": 45.00,
    "Waakye (plate)":25.00,
    "Fufu portion": 35.00
}
cart = [
    "Ankara fabric",
    "Plantain chips (pack)",
    "Palm oil (1L)",
    "Fufu portion",
    "Fufu portion"
]
item_quantity = {}
total = 0 

# Loop to calculate total and item quantity
for item in cart:
    if item in products:
        total += products[item]
        if item in item_quantity:
            item_quantity[item] += 1
        else:
            item_quantity[item] = 1
    else:
        print(f"Sorry, {item} is not in our store right now")

# Condition for discount
if total > 200:
    discount = 0.1
elif total > 100:
    discount = 0.05
else: 
    discount = 0

discount_amount = total * discount 
total_amount_to_pay = total - discount_amount 

# Final Summary
print("ORDER SUMMARY")
print("_"*30)
print("Products       quantity")
print("_"*30)

for item, quantity in item_quantity.items():
    print(f"{item} ----> {quantity}")

print("_"*30)
print(f"Total amount = {total}")
print(f"Discount = {discount_amount}")
print(f"Final amount to pay = {total_amount_to_pay}")
print("_"*30)