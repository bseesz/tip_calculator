# greeting
print("Welcome to the tip calculator!")

# get user input: total bill, tip percentage and total people
total_bill = (float(input("What was the total bill?: $ ")))
tip = (float(input("What percentage tip would you like to give? 10, 12, or 15: ")))
total_people = (int(input("How many people to split the bill?: ")))

# calculate tip and bill
# use round function to round two places
total_tip = round(total_bill * tip/100, 2)

split = round((total_bill + total_tip)/total_people,2)

# format to have two decimal places even with an ending zero
final_amount = "{:.2f}".format(split)

print(f"Each person should pay: ${final_amount}")

