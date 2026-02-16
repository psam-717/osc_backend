def calculate_cart_total(cart: list[str], products: dict[str, float]) -> float:
    subtotal = 0
    for cart_item in cart:
        if cart_item in products:
            subtotal += products[cart_item]
    return subtotal
    

# example
cart_demo = ["Apple", "Mango", "Watermelon", "Watermelon", "Grape", "book", "pen"]
products_demo = {
    "Apple": 20,
    "Mango": 35,
    "Watermelon": 40,
    "Pear": 50
}

print(calculate_cart_total(cart_demo, products_demo))
        

     
