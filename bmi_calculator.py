
                                    # BMI Calculator
    
# Ask for user's name
name = input("Enter your name: ")

# Ask for user's age
age = input("Enter your age: ")

# Ask user to choose units for weight and height
unit = input("Choose your units:\n1. KG/CM\n2. LB/FT\n")

# Input validation for weight
while True:
    weight = input("Enter your weight: ")
    try:
        weight_val = float(weight)  # Try converting input to float
        if weight_val > 0:          # Value must be positive
            break
        else:
            print("Value must be greater than 0!")
    except ValueError:
        print("Please enter a valid number!")

# Input validation for height
while True:
    height = input("Enter your height: ")
    try:
        height_val = float(height)   # Try converting input to float
        if height_val > 0:           # Value must be positive
            break
        else:
            print("Value must be greater than 0!")
    except ValueError:
        print("Please enter a valid number!")

# Unit conversion based on user choice
if unit == "1":
    height_val = height_val / 100    # Convert cm to meters
elif unit == "2":
    weight_val = weight_val * 0.453592   # Convert lbs to kg
    height_val = height_val * 0.3048     # Convert feet to meters

# Calculate BMI
bmi = weight_val / (height_val ** 2)

# Print the result with personalized message
print(f"{name}, age {age}, your BMI is: {bmi:.2f}")
