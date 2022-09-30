## 6.0001 Pset 1: Part a 
## Name: Karen Andre
## Time Spent: 30 minutes
## Collaborators: None

##########################################################################
## Get user input for annual_salary, portion_saved and total_cost below ##
##########################################################################
annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the portion of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))

#########################################################################
## Initialize other variables you need (if any) for your program below ##
#########################################################################
portion_down_payment = 0.20
current_savings = 0.0   # initialized as a float because rate of return adds a float to this value
r = 0.04
months = 0  # integer value that represents how many months we have been saving for
monthly_salary = annual_salary/12   # used to calculate the amount added to current_savings each month
down_payment = portion_down_payment * total_cost # the value of the down payment

###############################################################################################
## Determine how many months it would take to get the down payment for your dream home below ## 
#############################################################################################
while (current_savings < down_payment):
    months += 1 # we need to save for another month
    current_savings += current_savings*r/12 # monthly return due to interest, beginning of month savings used to calculate this
    current_savings += monthly_salary * portion_saved   # portion of salary added to savings

print("Number of months:", months)
