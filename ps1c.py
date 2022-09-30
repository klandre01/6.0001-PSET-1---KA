## 6.0001 Pset 1: Part c
## Name: Karen Andre
## Time Spent: 1:30
## Collaborators: None

##############################################
## Get user input for initial_deposit below ##
##############################################
initial_deposit = float(input("Enter the initial deposit: "))

#########################################################################
## Initialize other variables you need (if any) for your program below ##
#########################################################################
months = 36 # goal amount of months it takes to save enough for down payment
total_cost = 800000 # total cost of the house
portion_down_payment = 0.2 # percentage of the total cost used for down payment
down_payment = portion_down_payment * total_cost # total down payment for the house

##################################################################################################
## Determine the lowest rate of return needed to get the down payment for your dream home below ##
##################################################################################################
# current_savings = initial_deposit * (1 + r/12) ** months
high = 1.0 # highest possible rate of return
low = 0.0 # lowest possible rate of return
steps = 0 # amount of steps to find best r value
r = (high - low) / 2 # r is the rate of return, middle value of our range
current_savings = initial_deposit * (1+r/12) ** months # savings that our first guess yields
# check before beginning bisection search
if (initial_deposit >= down_payment):
    r = 0.0
elif (initial_deposit * (1 + 1.0/12)**months < down_payment): # if the best possible r yields less than down payment amount
    r = None
else: # if the initial deposit is less than the down payment and it is possible to save up in 36 months, continue with bisection search
    while (abs(current_savings - down_payment) > 100):  # while current savings is not within 100 dollars of the down payment
        # bisection search
        if (current_savings < down_payment):
            low = r # we need to guess higher numbers
        elif (current_savings > down_payment):
            high = r # we need to guess lower numbers
        r = (high + low) / 2  # update r value
        current_savings = initial_deposit * (1 + r/12) ** months    # update current savings
        steps += 1 # we have finished the first step

print("Best savings rate:", r)
print("Steps in bisection search:", steps)
