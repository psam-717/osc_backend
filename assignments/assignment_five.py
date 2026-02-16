from pprint import pprint

def calculate_cart_total(cart: list[str], products: dict[str, float]) -> dict:
    
    # to keep track of items in cart
    count = {}
    # stores absent items
    items_absent = []
  
    for item in cart:
        if item in products:
            if item in count:
                count[item] += 1
            else:
                count[item] = 1
        else:
            items_absent.append(item)
    
    cart_items = {}
    total = 0
    for item, qty in count.items():
        price = products[item]
        subtotal = qty * price
        total += subtotal
        
        cart_items[item] = {"quantity": qty, "price": price, "subtotal": subtotal}
       
    result = {
        "items": cart_items,
        "total_items": len(count),
        "subtotal": total,
    }
    
    if (len(items_absent) > 0):
        result["has_unknown_items"] = True
        result["unknown_items"] = items_absent
    else:
    
        result["has_unknown_items"] = False
    
    pprint(result, width=100)
    
    return result
    
            


cart_demo = ["Apple", "Mango", "Watermelon", "Pear","Watermelon", "Grape", "Pear"]
products_demo = {
    "Apple": 20,
    "Mango": 35,
    "Watermelon": 40,
    "Pear": 50
}

calculate_cart_total(cart_demo, products_demo)