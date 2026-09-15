# formula = kg/m^2

weight = float(input("Your weight (kg): "))
height = float(input("Your height (m): "))

BMI = weight/(height**2)
print(f"Your BMI is {BMI}.")
if BMI < 18.5:
    print("underweight")
elif BMI <24.9:
    print("normal")
elif BMI < 29.9:
    print("overweight")
else:
    print("obese")