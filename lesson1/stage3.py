'''Request 2 numbers
Request an operator for calculations (*, /, + and -)
Perform the appropriate calculations, based on the chosen operator'''
a, b = map(int, input("Enter 2 numbers: ").split())
operator = input()
if operator == "+":
    print(a+b)
elif operator == "*":
    print(a*b)
elif operator == "/":
    print(a/b)
else:
    print(a-b)

