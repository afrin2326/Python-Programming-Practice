#7.	Write a Python program to print all even numbers from a given list of numbers in the same order.

num=[1,2,3,4,5,6,7,8,9]

evens = [x for x in num if x % 2 == 0]
print(evens)