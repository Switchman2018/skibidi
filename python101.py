#!/bin/python3

#Print string
print("Strings and things:")
print("Hello World")
print("""Hello this is
a multi-line string""")
print("This is "+"a string")

print('\n') #new line

#Maths
print("Maths time:")
print(40 + 40) #add
print(40 - 40) #subtract
print(40 * 40) #multiply
print(40 / 40) #divide
print(40 + 40 - 40 * 40 / 40) #BOMDAS 
print(40 ** 2) #exponents
print(40 % 6) #modulo
print(40 // 6) #number without leftovers

print('\n') #new line

#Variables and methods
print("Fun with varibales and methods")
quote = "Pull hard, always, everytime"
print(len(quote)) #length
print(quote.upper()) #All upper case
print(quote.lower()) #All lower case
print(quote.title()) #Capitalises the first letter of each word

name = "Joseph"
age = 14 #int int(14)
gpa = 3.7 #float float(3.7)

print(int(age))
print(int(14.9)) #does nont round

print("My name is " + name + " and I am " +str(age) + " years old")

print('\n') #new line
age += 1
print(age)
birthday = 1
age += birthday
print(age)

print('\n') #new line

#Functions
print("Now some functions:")
def who_am_i():
	name = "Joseph"
	age = 14
	print("My name is " + name + " and I am " +str(age) + " years old")

who_am_i()

#Adding Parameters
def add_one_hundred(num):
	print(num + 100)

add_one_hundred(100)

#Adding mulltiple parameters
def add(x,y):
	print(x + y)

add(7,7)
add(305,207)

#Using Return
def multiply(x,y):
	return x * y

print(multiply(7,7))

def square_root(x):
	return x ** .5

print(square_root(64))

def NewLine():
	print('\n')

NewLine()

#Boolean expressions
print("Boolean Expressions")
bool1 = True
bool2 = 3*3 == 9
bool3 = False
bool4 = 3*3 != 9 #(! =) autocorrects to !=

print(bool1,bool2,bool3,bool4)
print(type(bool1))

bool5 = "True"  #Is now a string not a boolean
print(type(bool5))

#Relational and Boolean operators
greater_than = 7 > 5
less_than = 5 < 7
greater_than_equal_to = 7 >= 7
less_than_equal_to = 7 <= 7

print(greater_than,less_than,greater_than_equal_to,less_than_equal_to)

test_and = (7 > 5) and (5 < 7)
test_or = (7 > 5) or (5 < 7)
test_not = not True

print(test_and,test_or,test_not)

NewLine()

#Conditional Statements
print("Conditional Statements")
def soda(money):
	if money >= 2:
		return "You've got yourself a soda!"
	else:
		return "No soda for you poor boy"

print(soda(1))
print(soda(3))

NewLine()

def alcohol(age,money):
	if (age >= 18) and (money >= 5):
		return "You get vodka little boy"
	elif (age >= 18) and (money < 5):
		return "Poor Boy"
	elif (age < 18) and (money >= 5):
		return "Erm Guys, I think this ID is fake!"
	else:
		return "Leave little, young poor boy"

print(alcohol(18,5))
print(alcohol(18,4))
print(alcohol(17,5))
print(alcohol(17,4))

NewLine()

#Lists
print("Lists have brackets:")
movies = ["Star Wars Revenge of the Sith", "Star Wars a new hope", "Lord Of The Rings", "The Wolf of Wall Street"]

print(movies[0])
print(movies[0:3]) #add one more than you want
print(movies[1:])  #Slicing: up to but not including
print(movies[:1])
print(movies[-1])  #-1 pulls the last item in the list
print(len(movies))

movies.append("JAWS")
print(movies)

movies.pop() #if no number given thenn it removes the last item
print(movies)

movies.pop(2)
print(movies)

movies = ["Star Wars Revenge of the Sith", "Star Wars a new hope", "Lord Of The Rings", "The Wolf of Wall Street"]
person = ["Heath", "Jake", "Leah", "Jeff"]
combined = zip(movies, person)
print(list(combined))

NewLine()

#Tuples
print("Tuples have parentheses and cannot change")
grades = ("A", "B", "C", "D", "F")
print(grades[1])

NewLine()

#Looping
print("For loops - start to finish of iterate:")
vegetables = ["Cucumber", "Spinach", "Cabbage"]
for x in vegetables:      #iterating through list and printing all elemments
	print(x)

print("While loops - execute as long as true")
i = 1
while i < 10:
	print(i)
	i += 1
