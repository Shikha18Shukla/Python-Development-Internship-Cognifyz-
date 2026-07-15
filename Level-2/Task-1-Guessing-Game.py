import random

print("=" * 30)
print("      GUESS THE NUMBER")
print("=" * 30)

n = random.randint(1, 100)

while True:
    g = int(input("Enter your guess (1-100): "))

    if g == n:
        print("\n🎉 Congratulations!")
        print("You guessed the correct number.")
        break

    elif g < n:
        print("Too low! Try again.\n")

    else:
        print("Too high! Try again.\n")