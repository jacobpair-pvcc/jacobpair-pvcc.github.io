# Name: Jacob Pair
# Prog Purpose: This program finds the cost of the pet vaccines & medications for dogs and cats
#
# NOTE: Pet medications prescribed by licensed veterinarians are not subject to sales tax in Virginia
#
# PET CARE MEDS Pricing
#------------------------------------
# Canine Vaccines:
#   1. Bordatella $30.00
#   2. DAPP $35.00
#   3. Influenza $48.00
#   4. Leptospirosis $21.00
#   5. Lyme Disease $41.00
#   6. Rabies $25.00
#   7. Full Vaccine Package (includes all vaccines): 15% discount
#
# Canine Heartworm Preventative Chews (price per chew, one chew per month)
#   Small dogs, Up to 25 lbs: $9.99
#   Medium-sized dogs, 26 to 50 lbs: $11.99
#   Large dogs, $1 to 100 lbs: $13.99
#
# Feline Vaccines:
#   1. Feline Leukemia: $35
#   2. Feline Viral Rhinotracheitis: $30
#   3. Rabies (one year): $25
#   4. Full Vaccine Package (includes all vaccines): 10% discount
#
# Feline Heartworm Preventative Chews(one size): 8.00
#

import datetime

###############  define global variables ##############
# define dog prices
PR_BORD = 30
PR_DAPP = 35
PR_FLU = 48
PR_LEP = 21
PR_LYM = 41

PR_LEUK = 35
PR_VIRHI = 30
PR_RABIES = 25

PR_ALL = 0

PR_CHEWS_SMALL = 9.99
PR_CHEWS_MED = 11.99
PR_CHEWS_LARGE = 13.99

PR_CHEWS_OS = 8.00

#define global variables

############## define program functions ##################
def main():
    more = True
    while more:
        get_user_data()

    if pet_type.upper() == "D":
        get_dog_data()
        perform_dog_calculations()
        display_dog_results()
    else:
        get_cat_data()
        perform_cat_calculations()
        display_cat_results()

    askAgain = input("\nWould you like to prcoess another pet (Y/N)?: ")
    if askAgain.upper() == "N" :
        more = False
        print('Thank you for trusting PET CARE MEDS with your pet vaccines and medications.')

def get_user_data():
    global pet_name, pet_type, pet_weight
    pet_name = input("Pet name: ")
    pet_type = input("is this pet a dog (D) or cat (C)? ")
    pet_weight = input("weight of your pet (in pounds): ")

############### DOG functions ##################
    
def get_dog_data():
    global pet_vet_type, num_chews
    dog1 = "\n** Dog Vaccines: \n\t1.Bordatella \n\t2.DAPP \n\t3.Influenza \n\t4.Leptospirosis"
    dog2 = "\n\t5.Influenza \n\t6.Lyme Disease \n\t7.Rabies \n\t8.Full Vaccine Package \n\t9.NONE"
    dogmenu = dog1 + dog2
    pet_vax = int(input(dogmenu + "\n** Enter the vaccine number: "))

    print("\nMonthly heart worm prevention medication is recommended for all dogs.")
    heart_yesno = input("Would you like to order montly heartworm medication for " + pet_name + " (Y/N)? ")
    if heart_yesno.upper() == "Y":
        num_chews = int(input("How many heart worm chews would you like to order? "))

def perform_dog_calculations():
    global dog_vax_cost, dog_chews_cost, dog_total

    #### vaccines

    if pet_vax_type == 1 :
        dog_vax_cost = PR_BORD

    elif pet_vax_type == 2 :
        dog_vax_cost = PR_DAPP

    elif pet_vax_type == 3 :
        dog_vax_cost = PR_FLU

    elif pet_vax_type == 4 :
        dog_vax_cost = PR_LEP

    elif pet_vax_type == 5 :
        dog_vax_cost = PR_LYM

    elif pet_vax_type == 6 :
        dog_vax_cost = PR_RABIES

    else:
        PR_ALL = PR_BORD + PR_DAPP + PR_FLU + PR_LEP + PR_LYM + PR_RABIES
        dog_vax_cost = .85 * PR_ALL

    #### heart worm chews
    if num_chews != 0 :
        if pet_weight < 25 :
            dog_chews_cost = num_chews * PR_CHEWS_SMALL

        elif pet_weight >= 26 and pet_weight <50 :
            dog_chews_cost = num_chews * PR_CHEWS_MED

        else:
            dog_chews_cost = num_chews * PR_CHEWS_LARGE

    ####find total
    dog_total = dog_vax_cost + dog_chews_cost

def display_dog_results():
    print('Charlottesville Animal Hospital')
    print('Vaccine Amounts     $ ' + format(dog_vax_cost, '8,.2f'))
    print('Chews Amounts     $ ' + format(dog_chews_cost, '8,.2f'))
    print('Total Amount     $ ' + format(dog_total, '8,.2f'))
    print(str(datetime.datetime.now()))

################ CAT functions ###################
def get_cat_data():
    global pet_vet_type, num_chews
    cat1 = "\n** Cat Vaccines: \n\t1.Leukemia \n\t2.Viral Rhinotracheitis"
    cat2 = "\n\t3.Rabies \n\t4.Full Vaccine Package \n\t5.NONE"
    catmenu = cat1 + cat2
    pet_vax = int(input(catmenu + "\n** Enter the vaccine number: "))

    print("\nMonthly heart worm prevention medication is recommended for all cats.")
    heart_yesno = input("Would you like to order montly heartworm medication for " + pet_name + " (Y/N)? ")
    if heart_yesno.upper() == "Y":
        num_chews = int(input("How many heart worm chews would you like to order? "))

def perform_cat_calculations():
    global cat_vax_cost, cat_chews_cost, cat_total

    #### vaccines

    if pet_vax_type == 1 :
        cat_vax_cost = PR_LUEK

    elif pet_vax_type == 2 :
        cat_vax_cost = PR_VIRHI

    elif pet_vax_type == 3 :
        cat_vax_cost = PR_RABIES

    else:
        PR_ALL = PR_BORD + PR_DAPP + PR_FLU + PR_RABIES
        cat_vax_cost = .90 * PR_ALL

    #### heart worm chews
        cat_chews_cost = num_chews * PR_CHEWS_OS

    ####find total
    cat_total = cat_vax_cost + cat_chews_cost

def display_cat_results():
    print("DISPLAY CATS")
    print('Charlottesville Animal Hospital')
    print('Vaccine Amounts     $ ' + format(cat_vax_cost, '8,.2f'))
    print('Chews Amounts     $ ' + format(cat_chews_cost, '8,.2f'))
    print('Total Amount     $ ' + format(cat_total, '8,.2f'))
    print(str(datetime.datetime.now()))

##########  call on main program to execute ##########
main()

    


    
