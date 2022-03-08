#Below is the intro print statement
print("Welcome! This program will calculate the tip for your bill.\n")

print("In order to calculate your tip, we will need the following: \n\nTotal of the bill (in standard $xxxx.xx format--please do not include a dollar sign in your entry,  \nthe number of people splitting the bill--please use a whole number that is an integer, \nand the percentage of the tip--in a whole number that is an integer.")
# asking for the user input for the bill amount. I convert the entry into a float because of the potential two decimal place entry.
bill = float(input("Let's begin. What was the amount for the total bill? "))
people = int(input("How many people are going to split the bill? Please enter an integer only: "))
tip = int(input("What percentage would you like to tip? Ex: 10, 20, or 25 percent? Please enter an integer only: "))
tip_as_percent = tip / 100
total_tip_amt = bill * tip_as_percent
total_bill = bill + total_tip_amt
additional_tip = input("Would you like to change the tip percentage? (yes / no): ")
if additional_tip == "yes":
    tip = int(input("What percentage would you like to tip instead? Please enter an integer only: "))
    tip_as_percent = tip / 100
    total_tip_amt = bill * tip_as_percent
    total_bill = bill + total_tip_amt
    bill_per_person = total_bill / people
    final_amount = round(bill_per_person, 2)
    print(f"Each person should pay ${final_amount}")
else:
    bill_per_person = total_bill / people
    final_amount = round(bill_per_person, 2)
    print(f"Each person should pay ${final_amount}")

