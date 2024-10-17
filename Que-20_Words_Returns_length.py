'''
Write a Python function that takes a list of words and returns the length
of the longest one.
'''

words = ["apple", "banana", "watermelon", "cherry"]

max_length = 0

for word in words:
    if len(word) > max_length:
        max_length = len(word)

print("The length of the longest word is:", max_length)
