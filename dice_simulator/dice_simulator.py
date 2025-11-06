############################################################################################ DICE SIMULATOR ############################################################################################

import random


dice = []
number_of_dices = int(input("Choose how many dices you want: "))
total = 0



for i in range(number_of_dices):
    dice.append(random.randint(1, 6))
    
    
print(f"Rolls: {dice} \nTotal: {sum(dice)}")