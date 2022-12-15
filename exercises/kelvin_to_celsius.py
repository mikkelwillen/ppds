print("Temperature in Kelvin: ")
kelvin = input()
offset = -273.15

if kelvin.isdigit():
    print(f"Temperature in celsius: {float(kelvin) + offset:.2f}")
else:
    print("Please input a digit.")
