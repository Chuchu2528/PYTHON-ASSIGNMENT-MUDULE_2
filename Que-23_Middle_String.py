'''
Write a Python function to insert a
string in the middle of a string.
'''

insert_in_middle = lambda s, insert: s[:len(s)//2] + insert + s[len(s)//2:]

original_string = "hello world"
string_to_insert = " Python"

result = insert_in_middle(original_string, string_to_insert)
print(result)
