n = int(input("Enter the range: "))
a, b = 0, 1

print("The Fibonacci series up to", n, "is:")
print(a)
print(b)

for i in range(2, n):
    c = a + b
    
    print(c)
    a, b = b, c
