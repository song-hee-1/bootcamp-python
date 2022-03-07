#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the tip calculator.")
bill = input("What was the total bill? $")
tip_percentage = input("What percentage tip would you like to give? 10, 12, or 15? ")
people_num = input("How man people to split the bill? ")

bill_as_int = float(bill)
tip_percentage_as_float = float(int(tip_percentage) / 100)
people_num_as_int = int(people_num)

total_bill_person = (bill_as_int * ( 1 + tip_percentage_as_float )) / people_num_as_int
total_round = round(total_bill_person, 2)
print(f"Each person should pay: {total_round}$")


#Answer(Udemy)
# print("Welcome to the tip calculator!")
# bill = float(input("What was the total bill? $"))
# tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
# people = int(input("How many people to split the bill?"))

# tip_as_percent = tip / 100
# total_tip_amount = bill * tip_as_percent
# total_bill = bill + total_tip_amount
# bill_per_person = total_bill / people
# final_amount = round(bill_per_person, 2)

# print(f"Each person should pay: ${final_amount}")