### CAPSTONE PROJECT 1 - VARIABLES AND CONTROL STRUCTURES.
### Import math:

import math

### Give user choice of calculation.

print("Choose either 'investment' or 'bond' from the menu below to proceed:")
print("\n")
print("INVESTMENT - to calculate the amount of interest you'll earn on interest. \nBOND - to calculate the amount you'll have to pay on a home laon.")
print("\n")
calculation_type = input("Enter the Calculation you'd like to perform here:")

### If the user chooses investment:
### Ask user to input:
### Amount they are depositing

if calculation_type.lower() == "investment":
    amount_dep = float(input("Enter the amount you are depoisiting:"))
### Ask user to input:
### interest rate

    interest_rate = float(input("Enter the interest rate number only. No % sign required:"))/float(100)

### Number of years they plan on investing for

    years_inv = float(input("Enter the amount of years you plan to invest for:"))

### Simple or compound

    interest = input("Simple or compound interest:")

### based on user answer perform correct calcuation and print answer.
### simple interest calculation

    if interest.lower() == "simple":
        total_sim = amount_dep*(1 + interest_rate * years_inv)
        print("The total simple amount would be:",total_sim)

###compound interest calculation

    else:
        total_com = amount_dep * math.pow((1 + interest_rate),years_inv)
        print("The total compound amount would be:",total_com)    

###if user chooses bond:

elif calculation_type.lower() == "bond":

###get bond info from user

    house_val = float(input("What is the present value of your house?:"))
    b_int_rate = float(input("What is the interest rate?:")) / 12
    months = float(input("What is the number of months you plan to take to repay bond?:"))    

### calculate bond

    bond_total = (b_int_rate.house_val)/(1 - (1 + b_int_rate)^(- months))
    print("The total of the bond is:",bond_total)

    ###PROBLEM HERE^^^^^. For some reason I get an attribute error which says, '"float" object has no attribute "house_val"'
    ### I have tried to understand what the problem is but cannot figure it out. Please let me know what I am doing wrong and Ill correct it.
    
### if user does not enter 'investment' or 'bond':

else:
    print("error")
    




