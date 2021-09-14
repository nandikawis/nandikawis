#TASK 1

#Name                       : I PUTU NANDIKA WICAKSANA
#Student ID                 : e2000431
#Created on                 : 14/03/2021 
#Description of the program : This program will calculate parking fees in one day.

#line- "11": It print (-) symbol 58 times
#line- "12"-"16": It print intruduction messege of the program
#line- "17" : It print (-) symbol 58 times
print("-" * 58)
print('''
        WELCOME TO THE PARKING FEE COUNTER PROGRAM
                   THIS PROGRAM HELP TO
                 CALCULATE PARKING  COSTS
    ''')
print("-" * 58)

#line- "20" "main()" function is the primary function in this program
def main():

#line- "24" "Transaction" is variable that indicates 
# the total parking transaction in one day.    
    transaction = 0

#line- "28" "while True" is a looping statement that use to allow 
# repetition of calculating parking fare as long as the condition is True.    
    while True:

#line- "36" "input" is used to receive commands
#  from the user by what is stated in statement "input".  
#line- "37" This "if" syntax is used to read total transaction of the day 
# and it will count the number of times the transaction occurred.
#This "if" syntax will be executed if the user 
# press enter in vehicle "input" .
        vehicle = input("""Vehicle type <C>ar, <B>us, <T>ruck (<Enter> to quit): """).upper()
        if vehicle == "":
            if transaction == 0:
                print("""Parking lot 
                is closed for today...""")
                goo = False
            else:
                print("Total collection for to day : " + "RM " + str("{:.2f}".format(transaction)))
            break #this break is used to stop the reppetation all of the program

#line- "47"-"52" This "if" syntax will be executed if the user entered 
# the command that was explain in vehicle "input" statement.
        if vehicle == "C":
            vehic = "Car"
        elif vehicle == "B":
            vehic = "Bus"
        elif vehicle == "T":
            vehic = "Truck"

#line- "58" This ins_timeIn "input" is used to receive 
# the time enter from a vehicle.
#line- "59" This ins_timeOut "input" is used to receive 
# the time exit from a vehicle. 
        ins_timeIn = input("Time in (24-hour mode, e.g. 0900): ")
        ins_timeOut = input("Time out (24-hour mode, e.g. 1130): ")

#line- "63"-"69" This formula is used to represent the time in and time out 
# in 24-hour mode which consists of two-digit hour and two-digit minute.
        maxtimeIn = ins_timeIn.zfill(4)
        thourIn = int(maxtimeIn[0:2])
        tminuteIn = int(maxtimeIn[2:4])

        maxtimeOut = ins_timeOut.zfill(4)
        thourOut = int(maxtimeOut[0:2])
        tminuteOut = int(maxtimeOut[2:4])

#line- "78"-"95" This "if" syntax is used to check 
# the validate of time in and time out.
#In this "if" syntax there is a "continue". 
# It's used to stop the program from counting the entered time
# because it is invalid and returns to the previous "input".  
#In this "if" syntax there is a "pass". It's used to return 
# to the next program because the time is valid
        goo = True
        if (thourIn) > (24) or (tminuteIn) > (60):
            print("-Time in is not valid!")
            goo = False
        else:
            pass
        if (thourOut) > (24) or (tminuteOut) > (60):
            print("-Time out is not valid")
            goo = False
        else:
            pass
        
#This "if" syntax is used to stop the program because the time is more than one day.
        if int(maxtimeOut) == int(maxtimeIn) or int(maxtimeOut) < int(maxtimeIn):
            print("-Time out CANNOT be equal to or earlier than time in")
            goo = False
        else:
            pass

#line- "104"-"114" This "if" syntax is used to calculate total parking time.
# It's also distinguish total hour and total minute 
# of the parking time.
#"diffHour" variable that indicate total hour.
#"diffMinute" variable that indicate total minute.

        #This "if" syntax calculate if minute out more than minute in. 
        if (tminuteOut) > (tminuteIn):
            diffHour = (thourOut) - (thourIn)
            diffMinute = (tminuteOut) - (tminuteIn)
        #This "if" syntax calculate if minute out less than minute in.
        elif (tminuteOut) < (tminuteIn):
            diffHour = (thourOut) - (1) - (thourIn)
            diffMinute = (tminuteOut) + (60) - (tminuteIn)
        #This "if" syntax calculate if minute out is equal with minute in
        elif (tminuteOut) == (tminuteIn):
            diffHour = (thourOut) - (thourIn)
            diffMinute = (00)

#line- "118"-"121" This "if" syntax is used to 
# calculate roundedtime of the parking time  
        if diffMinute > (0):
            roundedTime = diffHour + (1)
        else:
            roundedTime = diffHour

#line- "127"-"156" This "if" syntax is used to calculate charges fee, 
# gst of charges fee and total after charges fee plus gst(6%). 
# Every vehicle has different charges fee, 
# so here will calculate charges fee of different vehicle.  
        if vehicle == "C":
            if roundedTime <= 3:
                charge = roundedTime * 0.80
                gst = charge * 0.06
                totalAll = charge + gst
            else:
                charge = (roundedTime * 1.50) - (3 * 1.50) + (3 * 0.80)
                #Here is calculate 3 hour before parking plus 3 hour after parking.
                gst = charge * 0.06
                totalAll = charge + gst
        elif vehicle == "B":
            if roundedTime <= 2:
                charge = roundedTime * 1.50
                gst = charge * 0.06
                totalAll = charge + gst
            else:
                charge = (roundedTime * 2.30) - (2 * 2.30) + (2 * 1.50)
                #Here is calculate 2 hour before parking plus 2 hour after parking.
                gst = charge * 0.06
                totalAll = charge + gst
        elif vehicle == "T":
            if roundedTime <= 1:
                charge = roundedTime * 2.00
                gst = charge * 0.06
                totalAll = charge + gst
            else:
                charge = (roundedTime * 3.40) - (1 * 3.40) + (1 * 2.00)
                #Here is calculate 1 hour before parking plus 1 hour after parking.
                gst = charge * 0.06
                totalAll = charge + gst

#line- "160"-"178" This "if" syntax is used to stop the 
# counting the entered time because the time is invalid.
        if thourIn > 24 and tminuteIn > 60:
            charge = 0
            gst = 0
            totalAll = charge + gst
            goo = False

        if thourOut < 24 and tminuteOut < 60:
            if maxtimeIn >= maxtimeOut:
                charge = 0
                gst = 0
                totalAll = charge + gst
                goo = False
            else:
                pass
        else:
            charge = 0
            gst = 0
            totalAll = charge + gst
            goo = False

#line- "184"-"233" All of this part will show the bill of the parking fee.
# There is used .rjust() string method to returns 
# a right justified version of the string.
        #There is to show (~) symbol 23 times.
        if goo == True:
            print("~" * 23)
        
            #There is to show "HELP PARKING LOT CHARGE".
            print("HELP PARKING LOT CHARGE")
        
            print("")
        
            #There is to show the type of the vehicle 
            # that was calculate in the bill.
            print("Type of vehicle: " + vehic.rjust(6))
        
            print("")
        
            #There is to show the time of the vehicle out.
            print("TIME-OUT " + (maxtimeOut[0:2] + ":" + maxtimeOut[2:4]).rjust(14))
        
            #There is to show the time of the vehicle in.
            print("TIME-IN " + (maxtimeIn[0:2] + ":" + maxtimeIn[2:4]).rjust(15))
        
            #There is to show (-) symbol 23 times.
            print(("-" * 6).rjust(23))
        
            #There is to show total of the parking time.
            print("PARKING TIME " + (str(diffHour).zfill(2) + ":" + str(diffMinute).zfill(2)).rjust(10))
        
            #There is to show total hour that the vehicle was parking.
            print("ROUNDED HOUR " + (str(roundedTime)).rjust(10))
        
            #There is to show (-) symbol 7 times.
            print(("-" * 7).rjust(23))

            #There is to show total charge.
            print("TOTAL CHARGE " + ("RM").rjust(5) + ("{:.2f}".format(charge)).rjust(5))

            #There is to show the gst of total charge.
            print("GST (6%) " + ("RM ").rjust(10) + ("{:.2f}".format(gst)).rjust(4))

            #There is to show (-) symbol 23 times.
            print(("-" * 7).rjust(23))

            #There is to show the total of total charge plus gst.
            print("TOTAL : " + ("RM").rjust(10) + ("{:.2f}".format(totalAll)).rjust(5))

            #There is to show (~) symbol 23 times
            print("~" * 23)
            print("")
        else:
            goo == False
            pass

#line- "237" There is a formula that will calculate 
# total income of the days
        transaction = transaction + totalAll
main()