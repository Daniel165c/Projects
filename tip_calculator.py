#Below is the intro print statement
print("Welcome! This program will calculate the tip for your bill.\n")

print("In order to calculate your tip, we will need the following: \n\nTotal of the bill (in standard $xxxx.xx format--please do not include a dollar sign in your entry,  \nthe number of people splitting the bill--please use a whole number that is an integer, \nand the percentage of the tip--in a whole number that is an integer.")
#Asking for user input which coverts it into a float.
bill = float(input("Let's begin. What was the amount for the total bill? "))
#asking for user input for amount of people splitting bill which coverts it into an integer
people = int(input("How many people are going to split the bill? Please enter an integer only: "))
#calculates the tax for the bill by multiplying by NYS sales tax
tax = bill * .08875
#new_bill is the original bill plus the tax costs
new_bill = bill + tax
#asking for user input regarding tip percentage
tip = int(input("What percentage would you like to tip? Ex: 10, 20, or 25 percent? Please enter an integer only: "))
#calculates tip percentage
tip_as_percent = tip / 100
#calculates the tip in dollars
total_tip_amt = new_bill * tip_as_percent
#calculates the new total bill
total_bill = new_bill + total_tip_amt
#asking user if they want to run the calculator over again and change the tip percentage.
additional_tip = input("Would you like to restart this application with a different tip percentage? (yes / no): ")
#starting if else loop. If user input is yes then app prompts user for new percentage and converts to integer
if additional_tip == "yes":
    tip = int(input("What percentage would you like to tip instead? Please enter an integer only: "))
    tip_as_percent = tip / 100
    total_tip_amt = new_bill * tip_as_percent
    total_bill = new_bill + total_tip_amt
    bill_per_person = total_bill / people
    final_amount = round(bill_per_person, 2)
    print(f"Each person should pay ${final_amount}")
else:
    bill_per_person = total_bill / people
    final_amount = round(bill_per_person, 2)
    print(f"Each person should pay ${final_amount}")

