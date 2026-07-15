print("========== BASIC CALCULATOR ==========")

a = float(input("First number: "))
b = float(input("Second number: "))
op = input("Operator (+, -, *, /, %): ")

if op == "+":
    r = a + b
elif op == "-":
    r = a - b
elif op == "*":
    r = a * b
elif op == "/":
    if b != 0:
        r = a / b
    else:
        r = "Cannot divide by zero"
elif op == "%":
    if b != 0:
        r = a % b
    else:
        r = "Cannot divide by zero"
else:
    r = "Invalid operator"

print("Answer:", r)