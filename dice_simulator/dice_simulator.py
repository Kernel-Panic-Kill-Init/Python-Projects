import random    

def menu():
    while True:
        dice = []
        number_of_dices = int(input("Choose how many dices you want: "))
        main_menu = int(input(
            "Choose which dice you prefer:\n"
            "1. 4 \n"
            "2. 6 \n"
            "3. 8 \n"
            "4. 10 \n"
        ))

        dice_types = {1: 4, 2: 6, 3: 8, 4: 10}
        if main_menu in dice_types:
            sides = dice_types[main_menu]
            for i in range(number_of_dices):
                dice.append(random.randint(1, sides))
            print(dice)
            print(sum(dice))
        else:
            print("Invalid input. Try again!")

menu()
