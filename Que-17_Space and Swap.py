'''Write a Python program to get a single string from
two given strings,separated by a space 
and swap the first two characters of each string.'''

str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")

if len(str1) > 1:
    str1 = str1[1] + str1[0] + str1[2:]
if len(str2) > 1:
    str2 = str2[1] + str2[0] + str2[2:]

result = str1 + " " + str2
print(result)
