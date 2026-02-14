# variables, some data types (string, int, float, lists / tuples and object)
print("this is our first backend meeting")


# variables 

# '+' : addition
# '-' : subtraction
# '*' : multiplication
# '**' : power

name_of_person = "marvin" 

nameOfPerson = "phil"

NameOfPerson = "kofi"

# print(nameOfPerson)
# print(NameOfPerson)
# print(name_of_person)



# Data types
# string => str
student_name = 'Marvinphil'




# float
area = 23.14567

# boolean => bool (either True or False)
is_student = False
is_HOD = True
# print(f"\n The datatype of {is_student} is ", type(is_student))

# kofi's school is KNUST
# print("\n Kofi's school is KNUST")
# print('\nThe man said "Hello" ')

# list => list 
fruits = ["apple", "mango", "watermelon"]
# print(f"\nThe datatype of {fruits} is :", type(fruits))



scores = [90, 70, 43]


# print(f"\nThe datatype of {cwas} is :", type(cwas))


# dictionary => dict
student_data = {"name": "Marvin", "age": 22, "class": "CS4"}
# print(f"\nThe datatype of {student_data} is: ", type(student_data))


# conditional statements and loops


# conditional statements

# if - else
# integer => int

print("\n")
student_age = 15



# if(student_age >= 18): 
#     print("You are an adult")
# elif (student_age < 16):
#     print("You are supposed to be in SHS")
# else:
#     print("You are not an adult")
    


# for loop

cwas = [67.8, 71.67, 82.24, 50.00, 47.8]
for any_cwa in cwas:
    print(any_cwa)


print("\n")
for any_cwa in cwas:
    if (any_cwa >= 70.00):
        print(f"{any_cwa}: First class")
    elif (any_cwa >= 60.00):
        print(f"{any_cwa}: Second class upper")
    elif (any_cwa >= 50.00):
        print(f"{any_cwa}: second class lower")
    else:
        print(f"{any_cwa}: pass")

 



