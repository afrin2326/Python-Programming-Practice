"""
def display():
    print("Afrin Binte Amin")
display()
"""

""" Farenheit to Celcius
temp1=77
celcius1=(temp1-32)*5/9
print(celcius1)

"""

"""
def farenheit_to_celcius(farenheit):
    return(farenheit-32)*5/9

print(farenheit_to_celcius(95))
"""

"""
def get_greeting():
    return "Hello from a function"
message=get_greeting()
print(message)
"""

"""
def my_function():
    pass
"""

"""
def my_function(fname):
    print(fname+" Refsnes")
my_function("Emil")
"""


"""
def my_function(name):
  print("Hello", name)

my_function("Emil")
"""

"""
def my_function(name="Afrin"):
    print("Hello",name)
my_function("Sakeen")
my_function()
"""

"""
def my_function(animal, name):
  print("I have an", animal)
  print("My", animal+"'s name is", name)

my_function("Buddy", "dog")
"""
"""
def my_function(fruits):
    for fruit in fruits:
        print(fruit)
my_fruits=["apple","banana","cherry"]
my_function(my_fruits)
"""
"""
def display(animal,name):
    print("My",animal+"s name "+"is",name)
display("dog","buzo")
"""

"""
def my_function(a, b, /, *, c, d):
  return a + b + c + d

result = my_function(5, 10, c = 15, d = 20)
print(result)
"""

"""
def my_function(*, name):
    print("hello",name)
my_function(name = "Emil")

"""
"""
def display():
    return["apple","banana","cherry"]
fruits=display()
print(fruits[1])
"""

"""
def my_function():
  return (10, 20)

x, y = my_function()
print("x:", x)
print("y:", y)
"""

"""
def display(fruit):
   for i in fruit:
       print(i)

fruits=["apple","lichi","watermelon"]
display(fruits)
"""
"""
def my_function(person):
  print("Name:", person["name"])
  print("Age:", person["age"])

my_person = {"name": "Emil", "age": 25}
my_function(my_person)
"""

"""
def myfunc():
  x = 300
  def myinnerfunc():
    print(x)
  myinnerfunc()

myfunc()
"""


"""
x = 300

def myfunc():
  print(x)

myfunc()
print(x)

"""

"""
x=lambda a,b,c:a+b+c
print(x(8,8,0))
"""

"""
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
print(mydoubler(11))
"""
"""
numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)
"""

""
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
odd_numbers = list((filter(lambda x:x%2!=0 ,numbers)))
#print(odd_numbers)
