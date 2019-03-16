from myNewModule import myPersonalCalculator

print("Calculator opens : -----------------------------------------------------------")
myNumber = input("Enter the comma-separated numbers : ").split(",")
myNumber = list(map(int, myNumber))
print('''
OPERATIONS : 
Sum -> Summation of all Elements 
Product -> Product of all Elements
EvenSum -> Summation of Elements at Even Indices
Exit -> For Terminating Calculator
''')
myPersonalCalculator(input("Enter the operation"), *myNumber)


# -----This is another module / python file which i am importing

# from functools import reduce
# def myPersonalCalculator(operation, *operators):
#     if operation == "Sum":
#         print(f"Summation (Addition) of the Entered numbers {operators} = ", reduce(
#             lambda x, y: x+y, operators))
#     elif operation == "Product":
#         print(f"Product of the Entered numbers {operators} = ", reduce(
#             lambda x, y: x*y, operators))
#     elif operation == "EvenSum":

#         EvenIndexList = operators[0::2]
#         print(f"Sum of Numbers {operators} at Even-Indices = ",
#               reduce(lambda x, y: x+y, EvenIndexList))
#     elif operation == "Exit":
#         print("Calculator closed : -----------------------------------------------------------")
