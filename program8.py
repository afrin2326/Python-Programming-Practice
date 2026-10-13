'''
8.	Take a character as input and determine whether it is a vowel or not.
Therefore, print an appropriate message (vowel/not vowel).
'''
ch = input("Enter a character: ").lower()
if ch in 'aeiou':
    print("Vowel")
else:
    print("Not vowel")
