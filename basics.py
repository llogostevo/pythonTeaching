# ouput uses the print keyword
# inside the brackets you use a string parameter - "what you want goes between speach marks"

print("hello world")

# a variable can be used to store data, this is a named location in memory that can be changed during execution of the program
name = "bob"
name = "sarah"
print(name) # Sarah

# you can take input into a variable
name = input()
print(name) # will output the users input

# you can also provide a prompt 
name = input("What is your name: ")
print(name)

# you can perform calculations with mathmatical operators

print(1+2) # 3
print(1/2) # 0.5
print(1*2) # 2
print(2**2) # 4
print(2**3) # 8

print(2//2) # this is called div, result is: 1
print(4//2) # this is called div, result is: 2
print(6//2) # this is called div, result is: 3
print(9//2) # this is called div, result is: 4

print(2 % 2) # this is called mod, result is:  0
print(4 % 2) # this is called mod, result is:  0
print(6 % 2) # this is called mod, result is:  0
print(9 % 2) # this is called mod, result is:  1

# the computer follows Bidmas, you can use brackets to force the calculation and also make it easier to read

print(1+2/3)
print(1+(2/3))
print(6*10/7*2+6)
print(((6*10)/7)*(2+6))

'''
comments can be either multiline with 3 single quotes
this makes your code easier to understand and more maintainable
it helps you know what you have done
'''
# or you can comment in single lines with a hashtag

'''
multiline tend to introduce new code blocks are complex algorithms
'''
# hashtags would be for inline comments to support understanding

# inline comments either go the line before or on the same line as the code being explained. 

# inputting numbers
newNumber = input("Input a number: )

print(newNumber+newNumber) # if the input as 3 this would output 33

'''
this is because inputs are always taken as a string and so the inputted number is dealt with like a letter not a number
to fix this you need to cast, (convert) the number into an integer
'''
# int () casts a datatype to integer
# str () casts a datatype to string
# float () casts a datatype to a real number, floating point i.e. a decimal number

print(int(newNumber)+int(newNumber)) # would fix the above issue and output 6 for a value of 3 inputted

# you could do the cast at the input to make things easier
anotherNewNumber = int( input("Enter the number") ) 
'''
the above now casts the string input directly to an integer before saving it in the variable anotherNewNumber
'''

thisIsAVariable = "a value" # notice how I capitalise the variables
'''
this is a technique called camel casing, like the humps of a camel
it makes it easer to read your variables

variables, and all identifiers, should be sensible
'''

firstName = "Bob" # this makes it more maintainable as the variable has meaning
z = "Richards" # I would struggle to know what z stands for in this program

print(name+" "+z)

# That should be enough to get you through most of the early challenges. 







