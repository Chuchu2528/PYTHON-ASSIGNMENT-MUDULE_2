'''
Write a Python program to find the first appearance of the
substring'not' and 'poor' from a given string, if 'not'
follows the 'poor', replace the whole 'not'...
'poor' substring with 'good'. Return the resulting string.
'''
str1 = input("Enter a string: ")

poor_index = str1.find('poor')
not_index = str1.find('not')

if poor_index != -1 and not_index != -1:
    if not_index > poor_index:
        
        result = str1[:poor_index] + 'good' + str1[not_index + 3:]
    else:
        result = str1
else:
       result = str1
print(result)
