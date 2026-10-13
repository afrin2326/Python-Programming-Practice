'''
6.	Write a Python program to swap the values of two variables.
Try this exercise with and without using a function.
'''

a=3
b=9
a,b=b,a
print("After swapping a=",a,"b=",b)

def swap(x,y):
    x,y=y,x
    return x,y

a,b=swap(a,b)

print("After swapping a=",a,"b=",b)
