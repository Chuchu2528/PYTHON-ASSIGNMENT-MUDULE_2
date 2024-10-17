#Write python program that swap two number with temp variable and
#without temp variable.

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Before swapping
print("Before swapping:")
print("Number 1:", num1)
print("Number 2:", num2)

temp = num1
num1 = num2
num2 = temp

# After swapping
print("After swapping:")
print("Number 1:", num1)
print("Number 2:", num2)
