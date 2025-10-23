######################################################################## BMI Calculator ##############################################################################

# Taking the user's inputs

def info_gathering():
    while True:
        name = input("Enter your name: ") # Ask for user's name
        age = int(input("Enter your age: ")) # Ask for user's age
        unit = input("Choose your units: \n1. KG/CM\2. LG/FT\n") # Ask user to choose units for weight and height
        return name, age, unit

####################################################################### BMI Calculator ##############################################################################

# Input validation 

def get_positive_number(prompt):
    while True:
        value = input(prompt)
        try:
            val = float(value)
            if val > 0:
                return val
            else:
                print("Value must be greater than 0!")
        except ValueError:
            print("Please enter a valid number!")

####################################################################### BMI Calculator ##############################################################################

#Converting units

def convert_units(weight, height, unit):
    if unit == "1":
        height = height / 100 #Converting cm to m
    elif unit == "2":
        weight = weight * 0.453592 # Converting lb to kg
        height = height * 0.3048 # Converting ft to m
    return weight, height



 ####################################################################### BMI Calculator ##############################################################################

def calculate_bmi(weight, height):
    return weight / (height ** 2)     

 ####################################################################### BMI Calculator ##############################################################################

def age_check(age, name, bmi):
    if age < 65:
        print(f"Hi {name}! At your age of {age}, your BMI is {bmi:.2f}.")
        print("For your age, a healthy BMI range is typically between 18.5 and 24.9.")
        print("Note: BMI does not account for muscle mass or physical activity. Interpretation can vary for athletic or muscular individuals.")
    else:
        print(f"Hi {name}! At your age of {age}, your BMI is {bmi:.2f}.")
        print("For adults over 65, a healthy BMI range may be between 25 and 27, according to health recommendations.")
        print("Always consult a medical professional when interpreting BMI values.")

####################################################################### BMI Calculator ##############################################################################

def main():
    name, age, unit = info_gathering()
    weight_val = get_positive_number("Enter your weight: ")
    height_val = get_positive_number("Enter your height: ")      
    weight_val, height_val = convert_units(weight_val, height_val, unit)
    bmi = calculate_bmi(weight_val, height_val)
    print(f"Hi {name}! Your BMI is {bmi:.2f}")
    age_check(age, name, bmi)

if __name__ == "__main__":
    main()
 ####################################################################### BMI Calculator ##############################################################################


####################################################################### BMI Calculator ##############################################################################




 ####################################################################### BMI Calculator ##############################################################################
