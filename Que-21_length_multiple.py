reverse_if_multiple_of_4 = lambda s: s[::-1]if len(s) % 4 == 0 else s

test_string = "abcd"
result = reverse_if_multiple_of_4(test_string)
print(result) 
