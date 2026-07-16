print("=" * 35)
print("    PASSWORD STRENGTH CHECKER")
print("=" * 35)

p = input("Enter your password: ")

u = l = d = s = 0

for i in p:
    if i.isupper():
        u = 1
    elif i.islower():
        l = 1
    elif i.isdigit():
        d = 1
    else:
        s = 1

if len(p) >= 8 and u and l and d and s:
    print("\nStrong Password ✅")
elif len(p) >= 6 and (u + l + d + s) >= 3:
    print("\nMedium Password ⚠️")
else:
    print("\nWeak Password ❌")