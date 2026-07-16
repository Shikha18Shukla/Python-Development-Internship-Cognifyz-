print("=" * 35)
print("      FIBONACCI SEQUENCE")
print("=" * 35)

n = int(input("Enter the number of terms: "))
a = 0
b = 1
print("\nFibonacci Sequence:")
for i in range(n):
    print(a, end=" ")
    c = a + b
    a = b
    b = c