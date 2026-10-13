'''
12.	Write a Python function (user defined/not built-in) to
find the maximum and minimum numbers from a sequence of numbers.
'''

def max_num(seq):
    return max(seq)
numbers1=[2,9,3,-3,5,1]
maximum=max_num(numbers1)
print("Maximum :",maximum)

def min_num(seq):
    return min(seq)
numbers2=[2,9,3,-3,5,1]
minimum=min_num(numbers2)
print("Maximum :",minimum)