import os

target_directory = "Days"





try:
    os.chdir(target_directory)

    #current_dir = os.getcwd()
    #print(f"Successfully changed directory to: {current_dir}")

    new_directory = input("Which day is is? (write it with 3 digits, example: 003\n")
    new_directory = new_directory + "Day"   
    os.mkdir(new_directory)

    exercise_num = input("What's the number of exercises")

except FileNotFoundError :
    print(f"ERROR : The directory '{target_directory}' was not found!")

except OSError as e:
    print(f"ERROR : Error chaning directory: {e}")