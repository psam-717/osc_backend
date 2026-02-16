def is_eligible_for_discount(subtotal: float, min_for_any_discount: float = 100.0) -> bool:
    if subtotal > min_for_any_discount:
        return True

   


def get_discount_percentage(subtotal: float) -> float:
    is_eligible = is_eligible_for_discount(subtotal, 100)
    if (is_eligible):
        if (subtotal > 250):
            subtotal *= 0.15 
        elif (subtotal > 180):
            subtotal *= 0.10
        else:
            subtotal *= 0.05
        return subtotal
    else:
        return 0
        


print(get_discount_percentage(370))
      