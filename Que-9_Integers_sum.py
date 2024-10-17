# Write a Python program to sum of three given integers. 
# However, iftwo values are equal sum will be zero.

num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))
num3 = int(input("Enter the third integer: "))

if num1 == num2 or num1 == num3 or num2 == num3:
    sum_of_numbers = 0
else:
    sum_of_numbers = num1 + num2 + num3


print("The sum of the three integers is:", sum_of_numbers)
