'''
Write a Python program to count the number of characters (character
frequency) in a string
'''
user_string = input("Enter a string: ")

frequency_dict = {}

for char in user_string:
    if char in frequency_dict:
            frequency_dict[char] += 1
    else:
        frequency_dict[char] = 1

print("Character Frequency:")
for char, count in frequency_dict.items():
    print(f"'{char}': {count}")
