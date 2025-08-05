#To avoid collision in executing the codes try Lshft+Entr at the end of each code line 

#A variable is automatically created when using '=' to assign a value to an identifier
speed = 80
ratio = 1.6
name = "metric"

#Using print() we can show the value of a variable
print("The speed in metric unit is:",speed*ratio,"KMH")

#Deleting python variables
del name
#print(name)    #Error if deleted

#Getting type of a variable
print(type(ratio))

#Casting variables
name = str('Sage')
age = str('21')
height = float('178.0')
#print("Correct age is =",age+2)     #Error because it is not an integer
print('Hello my names is',name,'and i am '+age,'years orld.')       #We can use + on str to str

#Multiple assignments
a, b, c = 10, 11, 12
print(a, b, c)

#Naming patterns
'''
    camelCase
    PascalCase
    snake_case
'''

#Local variables (can only be accessed inside the block)
def sum(x, y):
    sum = x + y
    return sum
print(sum(5, 7))

#Global variables (can be accessed everywhere)
a = 10
b = 10
c = 10
def sum():
    sum = a + b + c
    return sum
print(sum())