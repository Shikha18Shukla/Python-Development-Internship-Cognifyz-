print("=" * 35)
print("      WORD COUNTER")
print("=" * 35)

f = input("Enter the file name: ")

w = {}

with open(f, "r") as x:
    for l in x:
        for i in l.lower().split():
            i = i.strip(".,!?;:\"'()[]{}")
            if i:
                w[i] = w.get(i, 0) + 1

print("\nWord Occurrences:\n")

for k in sorted(w):
    print(f"{k:<15} {w[k]}")