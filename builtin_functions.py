def add_two(a,b):
    '''
    Description: sums the inputs
    input: 2 values
    Side Effect: none
    Return: sum of inputs
    '''
    return a+b

def main():
    # Put some stuff here

    #test cases for add_two
    print(add_two(3,7)) #Expecting 10
    print(add_two(0,0)) #Expecting 0
    print(add_two(-2, 5)) #Expecting 3

main()

def absolute_difference(x, y):
    '''
    Task: find the absolute difference between two numbers
    Name: absolute_difference
    Input: x, y
    Side Effects: no
    Return: non-negative difference
    '''
    return abs(x - y)


def smallest_of_three(a, b, c):
    '''
    Task: find the smallest of three numbers
    Name: smallest_of_three
    Input: a, b, c
    Side Effects: no
    Return: smallest number
    '''
    return min(a, b, c)


def count_characters(line):
    '''
    Task: count the characters in a string
    Name: count_characters
    Input: line
    Side Effects: no
    Return: number of characters
    '''
    return len(line)


def apply_tax(price, tax_rate):
    '''
    Task: calculate the total price after tax
    Name: apply_tax
    Input: price, tax_rate
    Side Effects: no
    Return: total price rounded to two decimal places
    '''
    total = float(price) * (1 + float(tax_rate))
    return round(total, 2)


def double_string_int(digits):
    '''
    Task: convert a string to an integer and double it
    Name: double_string_int
    Input: digits
    Side Effects: no
    Return: doubled integer
    '''
    return int(digits) * 2


def join_with_space(left, right):
    '''
    Task: join two strings with a space
    Name: join_with_space
    Input: left, right
    Side Effects: no
    Return: joined string
    '''
    return left + " " + right


def main():
    '''
    Task: test all seven functions
    Name: main
    Input: none
    Side Effects: prints test results
    Return: none
    '''
def main():
    print(absolute_difference(10, 3)) # expected: 7
    print(absolute_difference(3, 10)) # expected: 7
    print(absolute_difference(1.5, 1.5)) # expected: 0.0
main()

def main():
    print(smallest_of_three(4, 9, 1)) # expected: 1
    print(smallest_of_three(0, 0, 0)) # expected: 0
    print(smallest_of_three(-5, 2, -1)) # expected: -5
main()

def main():
    print(count_characters("hi")) # expected: 2
    print(count_characters("")) # expected: 0
    print(count_characters("a b c")) # expected: 5
main()

def main():
    print(apply_tax(100, 0.0625)) # expected: 106.25
    print(apply_tax(10, 0)) # expected: 10.0
    print(apply_tax(19.99, 0.05)) # expected: 20.99
main()

def main():
    print(double_string_int("21")) # expected: 42
    print(double_string_int("0")) # expected: 0
    print(double_string_int("-4")) # expected: -8
main()

def main():
    print(join_with_space("Berkle", "e")) # expected: Berkle e
    print(join_with_space("Berkle", "y")) # expected: Berkle y
    print(join_with_space("hello", "world")) # expected: hello world
main()