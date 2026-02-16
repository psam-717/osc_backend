products = {

    'Ankara fabric': 120.50,
    'Plantain chips(pack)': 15.00,
    'Palm oil (1L)': 45.00,
    'Waakye (plate)': 25.00,
    'Fufu portion' : 35.00

}

cart = ["Ankara fabric", "Plantain chips(pack)", "Palm oil (1L)", "Fufu portion", "Fufu portion", "Gobe"] 

total = 0
count ={}
first = 1
#Calculate the toal price and the number of products
for i in cart:
    if i in products:
        
        price = products[i]
        total += price
        if i in count:
            count[i]+= 1
        else:
            count[i] = 1
    else:
        print(f'{i} not found in cart')

discount = 1
if total> 200:
    discount = 10
elif 100<total<=200:
    discount = 5
else:
    discount = 1

message = f"""
Items bought:{count}
Subtotal = {total}
Discount = {discount}%
Amount Payable = {(total*discount)-total}
"""
print(message)