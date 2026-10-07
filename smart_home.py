def cel_to_fah(celsius):
    '''
    Description: it covertsa celsius value to fahrenheit
    Input: temperature in celsius
    Side Effect: none
    Returen: equivlent temp in fah
    '''
    fahrenheit = (celsius * 9/5) +32
    return fahrenheit


def display_temp(current_temp):
    '''
    Description: dispaly the current temperature
    Input: current temperature
    Side Effects: priting the temp
    Return: none
    '''
    print("The current temp is:", current_temp)
    return None



temp = 0
f_degrees = cel_to_fah(temp)
display_temp(f_degrees)





# Assigning values to variables
name = "Samuel"
print(name)
# They can be reassigned!
name ="sam"
print(name)

print(3+2) # 3+2 evaluates to 5 and THEN is passed into print
print(5)


# Data types
print("3") # String
print(3) # Integer (whole real number)
print(True) # Boolean
print(False) # Boolean

print(3+3)
print("3" +"3") # Concatenation
print("3" + "3")
print()
print("Hello")
print("Hello" + "Sam")
print("Hello Sam")
print("Hello", "Sam", "How", "Are", "You")

print("Hello", end="")
print("World", end="")

print("Hello", "")


def