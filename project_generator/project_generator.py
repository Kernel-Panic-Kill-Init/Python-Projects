

        ################################################################ PROJECT GENERATOR ####################################################################################



import random
import csv
import pandas as pd
import os

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
                        df = pd.read_excel("projects.ods", engine = "odf") # Reading the .ods file                      # Calling function that shows all of the projects --- and why .ods? Bc I'm working on Linux ;v
                        df = df[['Project', 'Description']] # Only columns that I'm interested in, bc in other way pandas shows Undefined columns and it looks shitty
                        df = df.dropna(subset=['Project', 'Description'], how='all') #Remowes rows where both fields are empty
                        #pd.set_option("display.max_rows", None) # Showing all rows from the file
                        script_dir = os.path.dirname(os.path.abspath(__file__)) # Making sure that the file .ods will be found (I've fucked up and have had the "WTF" moment when it couldn't find the file xD)
                        file_path = os.path.join(script_dir, "projects.ods")
                        print(df)
                elif main_menu == "0":
                        print("Thanks for using this app. Hang tight.")
                break
        else:
                print("Choose the correct option!")
                
if __name__ == "__main__":
        menu()
        
        
     