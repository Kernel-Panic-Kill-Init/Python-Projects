            ######################################################### BMI Calculator ###############################################################



# Taking the user's inputs
def info_gathering():
    while True:
        name = input("Enter your name: ") # Ask for user's name
        age = input("Eneter your age: ") # Ask for user's age
        unit = input("Choose your units: \n1. KG/CM\2. LG/FT\n") # Ask user to choose units for weight and height
        return name, age, unit
  
  #################################################################################################################################################################
  
# Ask for user's name
 # name = input("Enter your name: ")

# Ask for user's age
# age = input("Enter your age: ")

# Ask user to choose units for weight and height
 # unit = input("Choose your units:\n1. KG/CM\n2. LB/FT\n")



# Input validation 

def get_positive_number(prompt):
    while True:
        value = input()
        try:
            val = float(value)
            if val > 0:
                return val
            else:
                print("Value must be greater than 0!")
        except ValueError:
            print("Please enter a valid number!")

weight_val = get_positive_number("Enter your weight: ")
height_val = get_positive_number("Enter your height: ")







#Converting units
def convert_units(weight, height, unit):#
    if unit == 1:
        height = height / 100 #Converting cm to m
    elif unit == 2:
        weight = weight * 0.453592 # Converting lb to kg
        height = height * 0.3048 # Converting ft to m
        
        



#while True:
#    weight = input("Enter your weight: ")
#    try:
 #       weight_val = float(weight)  # Try converting input to float
#        if weight_val > 0:          # Value must be positive
 #           break
 #       else:
#            print("Value must be greater than 0!")
#    except ValueError:
#        print("Please enter a valid number!")
#
# Input validation for height
#while True:
#    height = input("Enter your height: ")
#    try:
#        height_val = float(height)   # Try converting input to float
#        if height_val > 0:           # Value must be positive
#            break
 #       else:
#            print("Value must be greater than 0!")
 #   except ValueError:
 #       print("Please enter a valid number!")

# Unit conversion based on user choice
#if unit == "1":
#    height_val = height_val / 100    # Convert cm to meters
#elif unit == "2":
 #   weight_val = weight_val * 0.453592   # Convert lbs to kg
#    height_val = height_val * 0.3048     # Convert feet to meters

# Calculate BMI
bmi = weight_val / (height_val ** 2)

# Print the result with personalized message
print(f"{name}, age {age}, your BMI is: {bmi:.2f}")

# if int(age) < 65:
#     print(f"Hi {name}! At your age of {age}, your BMI is {bmi:.2f}.")
#     print("For your age, a healthy BMI range is typically between 18.5 and 24.9.")
#     print("Note: BMI does not account for muscle mass or physical activity. Interpretation can vary for athletic or muscular individuals.")
# else:
#     print(f"Hi {name}! At your age of {age}, your BMI is {bmi:.2f}.")
#     print("For adults over 65, a healthy BMI range may be between 25 and 27, according to health recommendations.")
#     print("Always consult a medical professional when interpreting BMI values.")
