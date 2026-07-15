import random

print("=" * 32)
print("       NUMBER GUESSER")
print("=" * 32)

s = int(input("Start of range: "))
e = int(input("End of range: "))
x = random.randint(s, e)
c = 0
g = None

while g != x:
    g = int(input(f"Guess a number between {s} and {e}: "))
    c += 1
    if g > x:
        print("Your guess is too high.\n")
    elif g < x:
        print("Your guess is too low.\n")
print(f"\nWell done! You found the number in {c} guesses.")