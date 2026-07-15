
print("===== Temperature Converter =====")

temperature = float(input("Enter the temperature value: "))
unit = input("Is the temperature in Celsius (C) or Fahrenheit (F)? ").strip().upper()

if unit == "C":
    converted = (temperature * 9 / 5) + 32
    print(f"\n{temperature:.1f}°C is equal to {converted:.1f}°F")

elif unit == "F":
    converted = (temperature - 32) * 5 / 9
    print(f"\n{temperature:.1f}°F is equal to {converted:.1f}°C")

else:
    print("\nInvalid unit entered.")
    print("Please enter only C for Celsius or F for Fahrenheit.")