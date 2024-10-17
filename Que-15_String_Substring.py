# Write a Python program to count occurrences of a 
# substring in a string.

main_string = input("Enter the main string: ")
sub_string = input("Enter the substring to count: ")

occurrences = main_string.count(sub_string)

print(f"The substring '{sub_string}' occurs {occurrences} time(s) in the main string.")
