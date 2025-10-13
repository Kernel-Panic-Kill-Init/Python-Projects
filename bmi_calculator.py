                                                # BMI Calculator

                                                # Validation for the inputs
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in cm"))

                                                # Converting cm to m
height_m = height / 100

                                                # Calculating BMI according to its formula
bmi = weight / (height_m ** 2)
print(f"Your BMI is: {bmi:.2f}")

if bmi < 18.5:
    print("Underweight")
elif 18.5 <= bmi < 25:
    print("Normal weight")
elif 25 <= bmi < 30:
    print("Overweight, try to exercise a bit!")
else:
    print("Obese, take care of your health!")
