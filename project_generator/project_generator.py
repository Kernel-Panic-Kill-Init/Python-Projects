################################################################ PROJECT GENERATOR ####################################################################################

# Importing necessary libraries
import random
import pandas as pd
import os
import ezodf

################################################################ PROJECT GENERATOR ####################################################################################

# Welcome message
print("Hello there! I see you're lazy and don't want to think too much? That's great because so am I! This is why I've done this app.")

############################################ Function to save DataFrame to ODS ############################################

def df_to_ods(df, filename):
    """
    Saves a pandas DataFrame to an ODS file.
    
    Args:
        df (pd.DataFrame): The DataFrame to save
        filename (str): The name of the output ODS file
    """
    # Create a new ODS document
    ods = ezodf.newdoc(doctype="ods", filename=filename)
    
    # Create a new sheet with size based on DataFrame dimensions (+1 for header row)
    sheet = ezodf.Sheet("Sheet1", size=(len(df.index)+1, len(df.columns)))
    
    # Add the sheet to the document
    ods.sheets += sheet
    
    # Write column headers to the first row (index 0)
    for c, col in enumerate(df.columns):
        sheet[0, c].set_value(col)
    
    # Write data rows starting from index 1
    for r, row in enumerate(df.itertuples(index=False)):
        for c, value in enumerate(row):
            sheet[r+1, c].set_value(value)
    
    # Save the ODS file to disk
    ods.save()

############################################ Main Menu ############################################

def menu():
    """
    Main application menu loop.
    Handles user input and executes corresponding actions.
    """
    while True:
        # Display menu options
        main_menu = input(
            "1. Select a project at random. \n"
            "2. Display project in progress. \n"
            "3. Display ended projects. \n"
            "4. Show all projects. \n"
            "0. Exit. \n"
            "Choose an option: "
        )
        
        # Option 1: Random project selection and transfer to "in progress"
        if main_menu == "1":
            # Load the projects file into a DataFrame
            df = pd.read_excel("projects.ods", engine="odf")
            
            # Extract the "Project" column and remove empty values
            projects = df["Project"].dropna().tolist()
            
            # Randomly select one project from the list
            random_project = random.choice(projects)
            print(f"Selected project: {random_project}")
            
            # Remove the selected project from the original DataFrame
            df_new = df[df["Project"] != random_project]
            
            # Save the updated list back to "projects.ods"
            df_to_ods(df_new, "projects.ods")
            
            # Add the selected project to "projects_in_progress.ods"
            try:
                # Try to load existing "in progress" file
                df_in_progress = pd.read_excel("projects_in_progress.ods", engine="odf")
                
                # Append the new project to the existing DataFrame
                df_in_progress = pd.concat([df_in_progress, pd.DataFrame({"Project": [random_project]})], ignore_index=True)
            except FileNotFoundError:
                # If file doesn't exist, create a new DataFrame with the project
                df_in_progress = pd.DataFrame({"Project": [random_project]})
            
            # Save the updated "in progress" file
            df_to_ods(df_in_progress, "projects_in_progress.ods")
            print("Project moved to 'projects_in_progress.ods'.")
        
        # Option 2: Display projects currently in progress
        elif main_menu == "2":
            try:
                # Load and display the "in progress" file
                df_in_progress = pd.read_excel("projects_in_progress.ods", engine="odf")
                print("\nProjects in progress:")
                print(df_in_progress)
            except FileNotFoundError:
                # Handle case where no projects are in progress yet
                print("No projects in progress yet.")
        
        # Option 3: Display ended/completed projects
        elif main_menu == "3":
            try:
                # Load and display the "ended projects" file
                df_ended = pd.read_excel("projects_ended.ods", engine="odf")
                print("\nEnded projects:")
                print(df_ended)
            except FileNotFoundError:
                # Handle case where no projects have been completed yet
                print("No ended projects yet.")
        
        # Option 4: Display all available projects
        elif main_menu == "4":
            # Load the main projects file
            df = pd.read_excel("projects.ods", engine="odf")
            
            # Select only the columns we're interested in
            df = df[['Project', 'Description']]
            
            # Remove rows where both Project and Description are empty
            df = df.dropna(subset=['Project', 'Description'], how='all')
            
            # Display the filtered DataFrame
            print("\nAll projects:")
            print(df)
        
        # Option 0: Exit the application
        elif main_menu == "0":
            print("Thanks for using this app. Hang tight.")
            break  # Exit the while loop and end the program
        
        # Handle invalid input
        else:
            print("Choose the correct option!")

# Entry point: run the menu function when script is executed directly
if __name__ == "__main__":
    menu()
