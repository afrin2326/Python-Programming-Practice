'''
14.	Write a Python program that will sort the numbers of a given list in
both ascending and descending order without modifying the original (given) list.
'''
list=[2,9,4,0,6,7,3]
asc=sorted(list)
desc=sorted(list,reverse=True)
print("Original:", list)
print("Ascending:", asc)
print("Descending:", desc)
