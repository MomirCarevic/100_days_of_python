def life_in_weeks(current_age) :
    number_of_weeks = (90 - current_age) * 52
    print(f"You have {number_of_weeks} weeks left.\n")

life_in_weeks(int(input("How old are you?\n")))