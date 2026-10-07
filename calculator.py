def addition(num1, num2):
    '''
    Description: simple calculation of numbers
    Input: two numbers
    Side Effects: none
    Return: calculation results
    '''

    addition = num1 + num2
    return addition

result = addition(10, 2)
print(result)

def subtraction(num1, num2):
    '''
    Description: simple calculation of numbers
    Input: two numbers
    Side Effects: none
    Return: calculation results
    '''

    subtraction = num1 - num2
    return subtraction

result = subtraction(10, 2)
print(result)


def multiplication(num1, num2):
    '''
    Description: simple calculation of numbers
    Input: two numbers
    Side Effects: none
    Return: calculation results
    '''

    multiplication = num1 * num2

    return multiplication

result = multiplication(10, 2)
print(result)


def division(num1, num2):
    '''
    Description: simple calculation of numbers
    Input: two numbers
    Side Effects: none
    Return: calculation results
    '''

    division = num1 / num2
    return division

result = division(10, 2)
print(result)



def main():
    first_val = int(input("what is the first number?"))
    sec_val = int(input("What is the second nuber?"))
    operator = input("what operation would you like? + / - * ")
    print(addition(first_val, sec_val))
    # Test Cases
    print(addition(5,3)) # expecting 8
    print(addition(5,3)) # expecting 3
    print(addition(5, -400)) # expecting -395


    print(sub(0,3))




main()
