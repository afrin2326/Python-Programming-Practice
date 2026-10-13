#9.	Write a Python program that accepts a filename from the user and prints the extension of the file.

filename = input("Enter filename: ")
extension = filename.split(".")[-1]
print("File extension:", extension)
