# Write a Python program that will return true 
# if the two given integervalues are equal or their sum or difference is 5.

def check_values(a, b):
    if a == b or (a + b == 5) or (abs(a - b) == 5):
        return True
    else:
        return False

num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))

result = check_values(num1, num2)
print(result)

