# Name: Jacob Pair
# Prog Purpose: This program computes PVCC college tuition & fees based on number of credits
#  PVCC Fee Rates are from: https://www.pvcc.edu/tuition-and-fees

import datetime
# define tuition & fee rates
RATE_TUITION_IN = 159.61
RATE_TUITION_OUT = 336.21
RATE_CAPITAL_FEE = 23.50
RATE_INSTITUTION_FEE = 1.75
RATE_ACTIVITY_FEE = 2.90

#define global variables
inout = 1 # 1 means in_state, 2 means out-of-state
numcredits = 0
scholarshipamt = 0


#############  define program functions  ################
def main():
    more = True
    
    while more:
        get_user_data()
        perform_calculations()
        display_results()
        
        yesno = input("\nWould you like to calculate tuition & fees for another student? (Y or N)? ")
        if yesno == "N" or yesno == "n":
            more = False
            print('Have a good day!')

def get_user_data():
    global inout, numcredits, scholarshipamt
    numcredits = int(input("Number of credits registered for: "))
    scholarshipamt = float(input("Scholarship amount recieved: "))

def perform_calculations():
    global inout, tuition_amount, fee_amount, total_amount, balance_amount

    if inout == 1 :
        inout = RATE_TUITION_IN

    elif inout == 2 :
        inout = RATE_TUITION_OUT

    tuition_amount = inout
    fee_amount = numcredits * RATE_CAPITAL_FEE
    total_amount = tuition_amount + fee_amount
    balance_amount = total_amount - scholarshipamt

def display_results():
    print('-------------------------------')
    print('**** PVCC Student Tuition and Fees ****')
    print('-------------------------------')
    print('Tuition Amount     $ ' + format(tuition_amount, '8,.2f'))
    print('Fee Amount     $ ' + format(fee_amount, '8,.2f'))
    print('Total Amount     $ ' + format(total_amount, '8,.2f'))
    print('Scholarship Amount     $ ' + format(scholarshipamt, '8,.2f'))
    print('Balance Amount     $ ' + format(balance_amount, '8,.2f'))
    print('---------------------------')
    print(str(datetime.datetime.now()))

##########  call on main program to execute ##########
main()


