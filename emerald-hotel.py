#Name: Jacob Pair
#Prog Purpose: This program reads in a hotel data file, performs calculations, and creates an HTML file for the results

import datetime

############ define rate tuples ############

#            SR  DR  SU
#             0   1   2
ROOM_RATES = (195,250,350)

#           s-tax   occ-tax
#              0      1
TAX_RATES = (0.065,0.11250)
 
########### define files and list ############
infile = "emerald.csv"
outfile = "emerald-web-page.html"

guest = []

############ define program functions ############
def main():
    read_in_guest_file()
    perform_calculations()
    open_out_file()
    create_output_html()
            
def read_in_guest_file():
    guest_data = open(infile, "r")
    guest_in   = guest_data.readlines()
    guest_data.close()

    #### split the data and insert into list called: guest
    for i in guest_in:
        guest.append(i.split(","))
        

def perform_calculations():
    global grandtotal
    grandtotal=0
    
    for i in range(len(guest)):
            room_type = str(guest[i][2])
            num_nights = int(guest[i][3])

            if room_type =="SR":
                subtotal = ROOM_RATES[0] * num_nights
#STUDENTS: COMPLETE THESE elif AND else statements
            elif room_type =="DR":
                subtotal = ROOM_RATES[1] * num_nights
            else: 
                subtotal = ROOM_RATES[2] * num_nights
                
#STUDENTS: COMPLETE THESE CALCULATIONS
            salestax  = subtotal * TAX_RATES[0]
            occupancy = subtotal * TAX_RATES[1]
            total     = subtotal + salestax + occupancy
             
            grandtotal += total
        
#STUDENTS: ADD THE REST OF THE append statements after this one
            guest[i].append(subtotal)
            guest[i].append(salestax)
            guest[i].append(occupancy)
            guest[i].append(total)
            guest[i].append(grandtotal)


def open_out_file():
    global f
    f = open(outfile, 'w')
    f.write('<html> <head> <title> Emerald Beach Hotel & Resort </title>\n')
    f.write('<style> td{text-align: center} </style> </head>\n')
    f.write('<body style = "margin:auto; max-width: 700px; color:black; text-align:center; background-color:#000000; background-image: url(hotelWAL.jpg); font-family: calibri; ">')  #STUDENTS: COMPLETE THIS STATEMENT
    
def create_output_html():
    global f
    
    currency="8,.2f"
    today = str(datetime.datetime.now()) 
    day_time = today[0:16]

    f.write('<h1> Emerald Beach Hotel and Resort</h1>')
    tr = '<tr><td>'
    td = '</td><td>'
    endtr = '</td></tr>\n'

 #STUDENTS: INSERT ALL THE MISSING f.write STATEMENTS HERE
    moneyFormat = '8,.2f'
    f.write('<table class="center" border="1" style="text-align:center">')
    f.write('<tr style="font-weight: bold; color: black; font-size: 120%;">' +
    '<td>Last Name</td><td>First Name</td><td># Nights</td><td>Subtotal</td>' +
    '<td>Sales Tax</td><td>Occupancy Tax</td><td>Total</td></tr>')
    for guest_line in guest:
        f.write('<tr><td>' + guest_line[0] + '</td>')
        f.write('<td>' + guest_line[1] + '</td>')
        f.write('<td>' + guest_line[3] + '</td>')
        f.write('<td>' + format(guest_line[4],moneyFormat) + '</td>')
        f.write('<td>' + format(guest_line[5],moneyFormat) + '</td>')
        f.write('<td>' + format(guest_line[6],moneyFormat) + '</td>')
        f.write('<td>' + format(guest_line[7],moneyFormat) + '</td>')
        f.write('</tr>')

    f.write('</table><br />')
    f.write("</body></html>")
    f.close()
    print('Open ' + outfile + ' to view data.')

##call on main program to execute##
main()

