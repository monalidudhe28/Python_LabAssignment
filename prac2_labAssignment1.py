V = float(input("Enter Voltage: "))
R = float(input("Enter Resistance: "))
I = V/R
print(f"Current is: {I:.2f} A")
if I < 0.5:
    print("Low current")
elif 0.5 <= I <= 2:
    print("Normal current")
else:
    print("High current")
