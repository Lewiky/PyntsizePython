#variable declaration 
a = "hello world"
#printing
print(a)
#Multivariable lists
b = [1,2,3,4,5]
b.append("hello") # b = [1,2,3,4,5,"hello"]

#fstrings
fstring = f"the value of a is {a}"

x = 5 
#if elif else and or
if x == 5 and True:
    print(x)
elif x == 10 or False:
    print(10)
else:
    print(x)    

#while loop
while x > 5 and a == "hello world":
    print(x)
    #decrement
    x += -1

#for loops
for i in range(0,100):
    print(i)

#exception handling
try:
    print(y)
#Except multiple exception types with tuples
except TypeError, Exception as e :
    print(e)

#lists, appending, sorting
my_list = [1,2,3,4,5]
my_list.append(6)
my_list.sort()
my_list[0] # 1 
my_list[:-1] # 4

#tuples, unpacking
my_tuple = (1,2,3)
x, y, z = my_tuple

#dictionaries, defining, adding
my_dict = {'key': 1,'key2': 2}
print(my_dict['key'])
my_dict['key3'] = 3

#defining functions
def function(arg1,arg2):
    """This is a docstring"""
    #tuple return
    return arg1,arg2

#unpacking tuple return
return1, return2 = function(1,2)

#swapping variables
return1, return2 = return2, return1

#kwargs (key-word arguments) 
def kwfunction(**kwargs):
    """** unpacks the dictionary so we can access it's elements in the function.
    kwargs is an implicit argument passed to all functions"""
    print(kwargs['hello'])

#passing arbitrary arguments to a function as keywords
kwfunction(hello='hello',hi='hi')

#Generators, the values are lazily evaluated and each item is only generated when needed
def generator_function():
    for i in range(0,100000000):
        #Yield keword marks a generator
        yield i 

#print the first 1000 items from the generator, but don't evaluate all 10000000 unless needed 
for i in generator_function():
    print(i)
    if i == 1000:
        #break out of for loop
        break

#file IO -- with .. as closes the file object at the end of the block and gives the name f to the object
with open('example.txt') as f:
    f.write('')

# the same as above but with explicit opening and closing of the file
file = open('example.txt')
file.close()

#importing packages
import sys

#accessing command line args
sys.argv[0]

#list comprehensions
sqaures = [x**2 for x in range(0,1000)]

list_2 = [1,2,3,4]
#mapping, lambda function
map(lambda x: x**2, list_2)


