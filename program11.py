#11.	Write a Python program to filter positive numbers from a list.

numbers=[3,-6,9,-0,8,-6]
positives=[num for num in numbers if num>0]
print("Positive numbers:", positives)