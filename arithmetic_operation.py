# Task 1: Create functions for arithmetic operations with parameters for two numbers


def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

#---------------------------------------------------------------------------
# Task 2: Implement user input to receive two numbers and perform arithmetic operations of their choice and call the associated function

name = input('Hello, welcome to your dynamic calculator. The only calculator you will ever need. But first, may I have your name? ')
print(f"Hello {name}! First, what I am going to ask is for you to input two numbers. Then I will ask what operation you would like to perform and finally, I will show you the results. Are you ready? Great! Let's get started!")

num1 = int(input('Please enter your first number: '))
num2 = int(input('Please enter your second number: '))

print(f'Great! You have entered {num1} and {num2}!') 

operation = int(input('Now, what operation would you like to perform? \nYou can choose from the following by entering the associated number: \n1. Addition \n2. Subtraction \n3. Multiplication \n4. Division \n' ))

if operation == 1:
    add_result = add(num1, num2)
    print(f'The result of adding {num1} and {num2} is {add_result}. Thank you for using the dynamic calculator! Tell your friends! Have a great day, {name}!')
elif operation == 2:
    subtract_result = subtract(num1, num2)
    print(f'The result of subtracting {num2} from {num1} is {subtract_result}. Thank you for using the dynamic calculator! Tell your friends! Have a great day, {name}!')
elif operation == 3:
    multiply_result = multiply(num1, num2)
    print(f'The result of multiplying {num1} and {num2} is {multiply_result}. Thank you for using the dynamic calculator! Tell your friends! Have a great day,  {name}!')
elif operation == 4:
    divide_result = divide(num1, num2)
    print(f'The result of dividing {num1} by {num2} is {divide_result}. Thank you for using the dynamic calculator! Tell your friends! Have a great day, {name}!')
else:
    print(f"I'm sorry {name}, but this is invalid input. Please try again. :(")





