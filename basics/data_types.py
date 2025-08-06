#Numeric data types
var1 = 1       # int data type
var2 = True    # bool data type
var3 = 10.023  # float data type
var4 = 10+3j   # complex data type

#String data type
'''
    Subsets of strings can be taken using the
    slice operator ([ ] and [:] ).

    The plus (+) sign is the string 
    concatenation operator and the 
    asterisk (*) is the repetition 
    operator in Python
'''
str = 'Hello World!'

print (str)          # Prints complete string
print (str[0])       # Prints first character of the string
print (str[2:5])     # Prints characters starting from 3rd to 5th
print (str[2:])      # Prints string starting from 3rd character
print (str * 2)      # Prints string two times
print (str + "TEST") # Prints concatenated string

#Sequence data types:
'''
    Sequence is a collection data type. 
    It is an ordered collection of items. 
    Items in the sequence have a positional index starting with 0. 
    It is conceptually similar to an array in C or C++. 
    There are following three sequence data types defined in Python.
'''
#List data type
list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']

print (list)            # Prints complete list
print (list[0])         # Prints first element of the list
print (list[1:3])       # Prints elements starting from 2nd till 3rd 
print (list[2:])        # Prints elements starting from 3rd element
print (tinylist * 2)    # Prints list two times
print (list + tinylist) # Prints concatenated lists

#Tuple data type
tuple = ( ['a', 'b', 'c', 'd'], 786 , 2.23, 'john', 70.2  )
tinytuple = (123, 'john')

print (tuple)               # Prints the complete tuple
print (tuple[0])            # Prints first element of the tuple
print (tuple[1:3])          # Prints elements of the tuple starting from 2nd till 3rd 
print (tuple[2:])           # Prints elements of the tuple starting from 3rd element
print (tinytuple * 2)       # Prints the contents of the tuple twice
print (tuple + tinytuple)   # Prints concatenated tuples

#Range data type >>> range(start, stop, step)
for i in range(5,25,2):
  print(i)

#Binary data types:
#Bytes data type (0 -255)

# Using bytes() function to create bytes
b1 = bytes([65, 66, 67, 68, 69])
print(b1)  

# Using prefix 'b' to create bytes
b2 = b'Hello'
print(b2)

#Bytearray data type

# Creating a bytearray from an iterable of integers
value = bytearray([72, 101, 108, 108, 111])  
print(value)  

# Creating a bytearray by encoding a string
val = bytearray("Hello", 'utf-8')  
print(val)  