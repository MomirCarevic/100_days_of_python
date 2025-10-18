print("Welcoe to the tip calculator!")

total_bill = float(input("What was the total bill?\n"))
tip = int(input("How much tip would you like to give? 10, 12 or 15?\n"))
people = int(input("How many people to split the bill?\n"))

total_tip = (total_bill/100)*tip
separate_bill = (total_bill+total_tip)/people

print(f"Each person should pay: ${round(separate_bill,2)}")
