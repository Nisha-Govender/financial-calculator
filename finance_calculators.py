import math

print("Investment & Bond Calculator\n") # title of programme

print("Choose either 'investment' or 'bond' from the menu below to proceed: \n") # print choices for user
print("investment - to calculate the amount of interest you'll earn on your investment.")
print("bond - to calculate the amount you'll have to pay on a home load.\n")
initial_choice = input("\n").lower() # input choice from user & standardise in lower case

### investment calculator 

if initial_choice == "investment" : # if choice was investment calc
    input_invest = int(input("How much money would you like to invest (R)? : ")) # input invest amt as integer
    interest = float(input("What interest rate (%) would you want to earn? : ")) # input interest % as float
    input_years = int(input("How many years do you plan on investing for? ")) # input invest years as integer
    interest_choice = input("What type of interest do you want to utilise (simple or compound)? ").lower() # input interest type & standardise in lower case

    if interest_choice == "simple": # if choice was simple interest
        simple_interest = round((input_invest * (1 + ((interest/100)*input_years))),2) # insert formula and round amt
        print("Your final investment amount will be R" + str(simple_interest)) # print statement + round amt
    else: # if choice was compounding interest
        compounding_interest = round((input_invest*math.pow((1 + (interest/100)),input_years)),2) # insert formula and round amt
        print("Your final investment amount will be R" + str(compounding_interest)) # print statement + round amt


### bond calculator

elif initial_choice == "bond": # if choice was bond calc
     present_value = int(input("Please enter the present value of the house: ")) # input pv amt as integer
     interest = float(input("Please enter the interest rate (%): ")) # input interest % as float
     interest_conversion = ((interest/12)/100) # dividing the annual interest rate by 12 and convert interest amount to percentage
     input_months = int(input("Please enter the number of months you plan on repaying the bond: ")) # input pmt days as integer
     bond_calc = round((present_value*((interest_conversion*(1 + interest_conversion) ** input_months)) / ((1 + interest_conversion) **input_months-1)),2) # insert formula and round amt
     print("Your monthly bond repayment will be R" + str(bond_calc)) # print statement + round amt

else :
    print("Invalid entry. Please choose 'Investment' or 'Bond'. ") # user enters anything other than 'Investment' or 'Bond'
