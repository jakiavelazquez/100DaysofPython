# Display a welcome message
print("Welcome to the tip calculator!")

# Prompt the user to enter the total bill and convert it to a float
bill = float(input("What was the total bill? $"))

# Prompt the user to enter the tip percentage (10, 12, or 15) and convert it to an integer
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))

# Prompt the user to enter the number of people to split the bill and convert it to an integer
people = int(input("How many people to split the bill? "))

# Calculate the tip percentage as a decimal
tip_percentage = tip / 100

# Calculate the total tip amount
total_tip_amount = bill * tip_percentage

# Calculate the grand total bill
total_bill = float(total_tip_amount + bill)  # Convert to float for consistency

# Calculate the bill per person
bill_per_person = total_bill / people

# Display the result with the bill per person rounded to two decimal places
print(f"Each person should pay: ${round(bill_per_person, 2):.2f}")