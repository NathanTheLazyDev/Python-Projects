print("Welcome to Nate's temperature converter!, Type x anytime to exit")
temp = ((input("Enter the temperature digit: ")))
temp1 = (input("Temperature scale to be converted\n(f - farenheit)\n(c - celsius)\n(k - kelvin): "))
temp2 = (input("Convert to what temperature scale\n(f - farenheit)\n(c - celsius)\n(k - kelvin): "))
#c
if temp1 == temp2:
    print("That's the same temperature!")
elif temp1 == "c" and temp2 == "f":
    print((int(temp) * 9/5) + 32)
elif temp1 == "c" and temp2 == "k":
    print(int(temp) + 273.15)
#f
elif temp1 == "f" and temp2 == "c":
    print((int(temp) - 32) * 5/9)
elif temp1 == "f" and temp2 == "k":
    print((int(temp) - 32) * 5/9 + 273.15)
#k
elif temp1 == "k" and temp2 == "f":
    print((int(temp) - 273.15) * 9/5 + 32)
elif temp1 == "k" and temp2 == "c":
    print(int(temp) - 273.15)
#x
elif temp == "x" or temp1 == "x" or temp2 == "x":
    exit()