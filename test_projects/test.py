
    
amounts = [10, "hundred", "80", 450, 9.50]


def calculate_total_expenses(expenses: list[float]):
    total = 0
    invalid_expenses = []
    valid_expenses = []
    
    for item in expenses:
        if isinstance(item, (float, int)):
            valid_expenses.append(item)
            total += item
        else: 
            invalid_expenses.append(item)
    # print(valid_expenses)
    return valid_expenses, total


data = calculate_total_expenses(amounts)
print(data)


# # separating valid from invalid amounts
# invalid_amounts = []
# valid_amounts = []
# for i in amounts:
#     if (type(i) is not int) and (type(i) is not float):
#         invalid_amounts.append(i)
#     else:
#         valid_amounts.append(i)
# print(invalid_amounts)
# print(valid_amounts)

# invalid_amounts.append("one")
# invalid_amounts.append("two")
# print(invalid_amounts)


# for i in invalid_amounts:
#     amounts.remove(i)
# print(amounts)