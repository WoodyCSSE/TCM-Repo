#!/bin/python3

#Programmer: Woody Tilbury

#Strings
#Print String
print("hi")
print("""this is
on two lines""") #triple quote for multi line

print("this string is "+"awesome!") #we can also concatenate
print('\n') #New line
print("test the new line out. ")

print('\n')
#Math
print(50 + 50) #add
print(50 - 50) #subtract
print(50 * 50) #multiply
print(50 / 50) #divide
print(50 + 50 - 50 * 50 / 50) #PEMDAS
print(50 ** 2) #exponents
print(50 % 6) #modulo - takes what is left over
print(50 / 6) #division with remainder (float)
print(50 // 6) #division with no remainder

print('\n')
#Variables and Methods
quote = "This is an epic quote"
print(quote)

print(quote.upper()) #uppercase
print(quote.lower()) #lowercase
print(quote.title()) #title case

print('\n')
name = "Woody" #string
age = 18 #int
gpa = 3.7 #float

print(int(age))
print(int(30.1))
print(int(30.9))

print("My name is " + name + " and I am " + str(age) + " years old.")

age += 1
print(age)

print('\n')
#Functions

def who_am_i(): #this is a function without perameters
	name = "Woody" #local variable
	age = 18
	print("My name is " + name + " and I am " + str(age) + " years old.")

who_am_i()

def add_one_hundred(num):
	print(num + 100)

add_one_hundred(100)

def multiply(x,y):
	return x * y

multiply(9,9)
print(multiply(9,9))

def nl(): #New Line
	print('\n')

nl()
#Boolean Expressions and Relational Operators

bool1 = True
bool2 = 3*3 == 9
bool3 = False
bool4 = 3*3 != 9

print(bool1,bool2,bool3,bool4)

bool5 = "True"
print(type(bool5))

nl()
#Relational and Boolean Operators
equal_to = 5 == 5
not_equal_to = 5 != 7 
greater_than = 7 > 5
less_than = 5 < 7
greater_than_equal_to = 7 >= 7
less_than_equal_to = 7<= 7

test_and = (7 > 5) and (5 < 7) #True
test_and2 = (7 > 5) and (5 > 7) #False
test_or = (7 > 5) or (5 < 7) #True
test_or2 = (7 > 5) or (5 > 7) #True
test_not = not True #False
test_not2 = not False #True

nl()
#Conditional Statements - if/then

def drink(money):
	if money >= 2:
		return "You can get a drink"
	else:
		return "Not enough"
print(drink(3))
print(drink(1))

def 
