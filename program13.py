#13.	Write a Python program to find the total number of even and odd numbers from a given list.

numbers=[2,5,3,8,9,4]
countEven=len([x for x in numbers if x % 2 == 0])
countOdd=len(numbers)-countEven
print("Even:", countEven)
print("Odd:", countOdd)