"""print [1,2,....,50]using  for or while loop"""
"""
no=1
while no<=50:
    print(no)
    no+=1
"""

"""
def exponentiation(a,b):
    return a ** b
print(exponentiation(7,2))
"""

def exponentiation_while(a, b):
    result = 1
    count = 0
    while count < b:
        result = result * a
        count += 1
    return result

print(exponentiation_while(7, 2))

