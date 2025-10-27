

        ################################################################ PROJECT GENERATOR ####################################################################################



import random
import csv
import pandas as pd

        ################################################################ PROJECT GENERATOR ####################################################################################

print("Hello there! I see you're lazy and don't want to think too much? That's great because so am I! This is why I've done this app.")

                                ############################################ Menu ############################################

def menu():
        while True:
                main_menu = input(
                        "1. Select a project at random. \n"
                        "2. Display project in progress. \n"
                        "3. Display ended projects. \n"
                        "4. Show all projects. \n"
                        "0. Exit. \n"
                        "Choose an option: "
                                  )
                if main_menu == "1":
                        pass
        # Random selection activation
                elif main_menu == "2":
                        pass
        # Showing project in progress
                elif main_menu == "3":
                        pass
        # Calling function showing ended projects
                elif main_menu == "4":
                        pass
        # Calling function that shows all of the projects
                elif main_menu == "0":
                        print("Thanks for using this app. Hang tight.")
                break
        else:
                print("Choose the correct option!")
                
if __name__ == "__main__":
        menu()