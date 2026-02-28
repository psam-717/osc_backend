products= {
    "Ankara Fabric" : 120.50,
    "Plantain chips" : 15.00,
    "Palm oil": 45.00,
    "Waakye": 25,
    "Fufu portion" : 35.00
}

carts= {}

subtotal= 0
discount = 0
cart = ["Ankara Fabric","Plantain chips","Palm oil", "Waakye", "Waakye","Fufu portion"]
counts= len(cart)

if cart == []:
    print("The cart is empty")
print(f"Your Cart items are:")    
for itm in cart:
    
    if itm in products:
        subtotal+=products[itm]
        if itm in carts:
            carts[itm] += 1
        
        else:
            carts[itm] = 1    

        
        
    else:
        print(f"{itm} does not exist in our store")
print(f"{carts}")
print(f"The number of items are {counts}")
print(f"The subtotal is {subtotal}")

if subtotal>200:
    print(f"Discount is 10%")
    discount = 0.01 * subtotal 
elif subtotal>100 and subtotal<=200:
    print("Discount is 5%")
    discount= 0.05 * subtotal

else:
    print("There is no discount")
    discount= 0
total=subtotal-discount
print(f"The total is {total}")