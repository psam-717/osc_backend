#My Consoled Budget Calculator


# i need to add sth  that is a  loop to it. This is what i have to do for  the day


categories={}





def get_month_budget():
    while True:
        try:
            salary= float(input("What is your monthly salary? "))
            if salary <= 0:
                print("Enter a positve number")
                continue  
        except ValueError:
            print("Please enter a number")
            continue
          
        return salary


def get_category_itm():

    
    while True:
    
        prompts = input("Enter a category name: ")
        
        if not prompts:
            print("Please Enter a category")
            continue
        category = {}
        while True:
            try:
                itm_name = input(f"What is the name the {prompts} category: ")
                itm_amt = float(input(f"Enter the amount of {itm_name}: "))
            except ValueError:
                print("Please enter a number")
                continue
            if itm_amt <= 0:
                print("Please enter a positive number")
                continue
            category[itm_name] = itm_amt
            cont = input("Do you want to add other items? ")
            if cont == "yes":
                continue
            else:
                break
        categories[prompts] = category
        
        cprompts = input("Do you want to add another category? ")
        if cprompts == "yes":
            continue
        else:
            break
    return categories



def cal_expenses(categories):
    total_expenses = 0
    for item in categories:
        for itm in categories[item]: 
            total_expenses += categories[item][itm]
    return total_expenses
 


def balance(salary,total):
    
    balanced =  salary - total
    return balanced

def display_cat(category):
    for cat, itms in categories.items():
        print(f"\nCategory: {cat}")   
        for name, amt in itms.items():
            print(f" {name}: {amt}")    
#summary
def display():
    print("Welcome to Personal Budget Calculator")
    named= input("What is your name? ")
    cal = get_month_budget()
    cals = get_category_itm()
    total = cal_expenses((cals))
    balancc = balance(cal,total)
    

    print(f"\n==========Budget Summary for {named}===========")
    print(f"Hello {named}")
    print(f"{display_cat(categories)}")
    print(f"          Monthly income: {cal}")
    print(f"          Total Expenses: {total}")
    print(f"          Revenue Budget: {balancc}")
   
    if balancc < 0:
        print(f"Your balance is {balancc}")
        print("You are out of budget")
    else:
        print(f"Your balance is {balancc}")
        print("Keep it up")
    return


print(display())
    