# a == b 
# a != b #not equal
# a > b #greater than
# a < b #less than
# a >= b #greater than or equal to
# a <= b #less than or equal to

# a = 30
# b = 30

# if a < b:
#     print("a is less than b")
# elif a == b:
#     print("a is equal to b")    
# else: 
#     print("a is greater than b")    

#Nested if statements
# x = 41 

# if x >10: 
#     print("x is greater than 10")
#     if x > 20:
#         print("x is greater than 20")
#     else: 
#         print("x is less than or equal to 20")    

age = 17
has_license = True

if age >= 18:
    if has_license: 
        print("You are eligible to drive.")
    else: 
        print("You need a driver's license to drive.")    

else: 
    print("You are not eligible to drive.")        