# Name: Jacob Pair
# Prog Purpose: This program finds the personal property tax for vehicles in Charlottesville
#   Price for one ticket: $10.99
#   Sales tax rate: 5.5%

import datetime

##############  define global variables  ##############
# define tax rate and tax relief
PER_PROP_TAXRATE = 4.20
TAX_RELIEF = .33

# define global variables
Date = 0
Assessed_Value = 0
Annual_Amount = 0
Relief_Amount = 0
total = 0

##############  define program functions  ##############
def main():

    amount_paid = True

    while amount_paid:
        get_user_data()
        perform_calculations()
        display_results()

        if Relief_Amount == "Y" or yesno == "Y":
            Relief_Amount = True
            Relief_Amount = .33

def get_user_data():
    global num_tickets
    num_tickets = int(input("Number of movie tickets: "))

def perform_calculations():
    global subtotal, sales_tax, total
    subtotal = num_tickets * PR_TICKET
    sales_tax = subtotal * SALES_TAX_RATE
    total = subtotal + sales_tax

def display_results():
    print('-------------------------------')
    print('**** CINEMA HOUSE MOVIES ****')
    print('Your neighbordhood movie house')
    print('-------------------------------')
    print('Tickets     $ ' + format(subtotal, '8,.2f'))
    print('Sales Tax     $ ' + format(sales_tax, '8,.2f'))
    print('Total     $ ' + format(total, '8,.2f'))
    print('---------------------------')
    print(str(datetime.datetime.now()))

##########  call on main program to execute ##########
main()


