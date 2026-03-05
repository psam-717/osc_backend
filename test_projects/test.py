
    
amounts = [10, "hundred", "80", 450, 9.50]

# extract numbers from the list

def nums_and_list_separation(dummy_list: list):
    nums_list = []
    strings_list = []
    for item in dummy_list:
        if isinstance(item, (float, int)):
            nums_list.append(item)
        else:
            strings_list.append(item)
    return nums_list, strings_list


nums_list_output, _ = nums_and_list_separation(amounts)
print()
print(nums_list_output)
        


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