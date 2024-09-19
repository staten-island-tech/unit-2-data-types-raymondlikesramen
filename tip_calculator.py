

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $70"))

tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
tip= 4

num_of_split = int(input("How many people to split the bill? 4."))
num_of_split=4

calculate_bill = bill * (1 + (tip/100)) / num_of_split

final_amount = "{:.2f}".format(calculate_bill, 2)

if tip == 10:
        print(f"Each person should pay: ${final_amount}")
elif tip == 12:
        print(f"Each person should pay: ${final_amount}")
else:
        print(f"Each person should pay: ${final_amount}")