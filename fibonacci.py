# Fibonacci sequence generator

digits =  input("How many digits? (enter an integer): ")
digits = int(digits)

a = 0
b = 1

for i in range(digits):
    print(str(a))
    a = a+b
    b = a-b