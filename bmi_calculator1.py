
# BMI Calculator


while True:  # Validation loop for weight input
    weight = input("Enter your weight in kg: ")
    if weight.isdigit() and float(weight) > 0:  # Prevents that the numbers are over 0
        weight = float(weight)
        break
    else:
        print("Please enter a valid number greater than zero!")

while True:  # Validation loop for height input
    height = input("Enter your height in cm: ")
    if height.isdigit() and float(height) > 0:  # Prevents that the numbers are over 0
        height_m = float(height) / 100  # Convert cm to meters
        break
    else:
        print("Please enter a valid number greater than zero!")

bmi = weight / (height_m ** 2)
print(f"Your BMI is: {bmi:.2f}")

if bmi < 18.5:
    print("Underweight.")
elif 18.5 <= bmi < 25:
    print("Normal weight.")
elif 25 <= bmi < 30:
    print("Overweight, try to exercise a bit!")
else:
    print("Obese, take care of your health!")



