#_______________________________________________________________________________
# Name: Abhinav Dinesh Sukhramani
# Date: 2/13/2018
# Course: ITMD-513
# Lab 4
#_______________________________________________________________________________

import os.path , time   #Package imprted to get current date and time modified
from random import *    # Generating random numbers
import copy

print('_____________________________________________________________________')
print('Name : Abhinav Dinesh Sukhramani')
print('Course: ITMD-513')
print('Lab-4')
print('Last Modified (Date and time): %s' %time.ctime(os.path.getmtime ("ads_lab4.py"))) # Retrieves the modification date and time
print('_____________________________________________________________________')



'''
_____________________________________________Main Menu________________________________________________________
'''
print('\n\n\n Welcome to generic lottery game! Kindly select from the following options:\n')
def ads_main_menu():

    print('1. Instructions\n 2. Pick 3 without Fireball ($0.50) \n 3. Pick 3 with Fireball ($1)\n 4. Exit ')
    ads_mm_ip = input('Enter: ')    #Input selection
    ads_mm_ip = int(ads_mm_ip)
    if(ads_mm_ip == 1):
        ads_instructions()
        ads_main_menu()
    elif(ads_mm_ip == 2):
        ads_p3_no_fb()
        ads_ch()
    elif(ads_mm_ip == 3):
        ads_p3()
        ads_main_menu
    elif(ads_mm_ip == 4):
        print('Thank You, Hope to see you again')
    else:
        print('Kindly Enter a valid Choice!')
        ads_main_menu()


'''
_____________________________________________Instructions________________________________________________________
'''

def ads_instructions():
    print('Here are the rules for the game:')
    print('-> User guesses 3 numbers and wins $100 if the numbers are similar to the ones that are drawn.')
    print('-> Fireball is an additional number drawn to increase the chances of winning (optional)')
    print('->If you have one dissimilar number that is matching with the fireball, you immediately win $100 ')
    print('->Additionally, if the numbers guessed by user match the numbers drawn and fireball, an additional $50 is added to the prize for every number matching the fireball')
    print('-> Let\'s play\n')


'''
_____________________________________________Choice after playing the game________________________________________________________
'''

def ads_ch():
    print('Would you like to play again?\n')
    ads_choice = input('y/n: ')
    if(ads_choice =='y'):
        ads_main_menu()
    elif(ads_choice == 'n'):
        print('Thank You For playing')
    else:
        print('Kindly enter a valid option')
        ads_ch()


'''
_______________________________________Pick 3 with fireball_________________________________________________
'''
def ads_p3():

    #------------------------VARIABLES
    #input
    ads_cnum1 = input('Enter 1st lottery number: ')
    ads_cnum2 = input('Enter 2nd lottery number: ')
    ads_cnum3 = input('Enter 3rd lottery number: ')
    ads_cnum1 = int(ads_cnum1)
    ads_cnum2 = int(ads_cnum2)
    ads_cnum3 = int(ads_cnum3)
    #numbers must be between 0 and 9
    if((ads_cnum1 < 0 or ads_cnum1 > 9) or (ads_cnum2 < 0 or ads_cnum2 > 9) or (ads_cnum3 < 0 or ads_cnum3 > 9)):
        print('Kindly select numbers between 0 and 9\n')
        ads_p3()
    else:
        #Initialize list
        ads_userpicks = list()
        #Add them in list
        ads_userpicks.append(ads_cnum1)
        ads_userpicks.append(ads_cnum2)
        ads_userpicks.append(ads_cnum3)
        print('\nUser picks: ',ads_userpicks)
        ads_userpicks.sort()    #Sort them in ascending order

    #----------------------- LOTTERY NUMBERS
    #Random Number generators
        ads_rnum1 = randint(0,9)
        ads_rnum2 = randint(0,9)
        ads_rnum3 = randint(0,9)

        ads_prize = 0   #Variable initialized for prize amount
        ads_prize = int(ads_prize)  #Lottery Prize

        #Fireball generator
        ads_fbnum = randint(0,9)
        #Initialize an empty list
        ads_randompicks = list()
        ads_randompicks.append(ads_rnum1)
        ads_randompicks.append(ads_rnum2)
        ads_randompicks.append(ads_rnum3)
        print('Lottery picks: ',ads_randompicks)
        ads_randompicks.sort()
        #---------------------------Display numbers


        print('Fireball pick: ',ads_fbnum)

        #--------------------------Create 2 lists & Copy Elements from both lists
        ads_cp_user = list(ads_userpicks)
        ads_cp_lt = list(ads_randompicks)

        #-------------------------Using while loop to iterate through list for comparison
        # Pointer variables
        i = 0
        i = int(i)
        j = 0
        j = int(j)

        #-----Selects a user number and compares it with every element in lottery list
        while ( i < len(ads_cp_user) ):
            j = 0   #Number list pointer goes back to 0
            while (j < len(ads_cp_lt)):
                if(ads_cp_user[i] == ads_cp_lt[j]):
                    ads_cp_user[i] = 'X'    # X = Y
                    ads_cp_lt[j] = 'Y'
                    break
                else:
                    j = j + 1
            i = i+ 1
        #-----------------------------end loops

        #print(ads_cp_user)
        #print(ads_cp_lt)
    #-----------------FINAL RESULT
        i = 0
        count = 0   # To count number of Y's in lottery
        count = int(count)
        while( i < len(ads_cp_lt)):
            if(ads_cp_lt[i] == 'Y'):
                count += 1
            i +=1

        #PRIZE ALLOCATION
        if(count == 3):
            ads_fb_count = int(0)
            z = int(0)  #Pointer for user numbers
            while(z < len (ads_userpicks)):
                if(ads_userpicks[z] == ads_fbnum):
                    ads_fb_count += 1
                z +=1
            ads_prize = 100 + (50 * ads_fb_count)
            if(ads_prize ==100):
                print('\nTough Luck with fireball but congratulations you win $',ads_prize,'\n\n')
            elif(ads_prize > 100):
                print('\n COngratulations!! ',ads_fb_count , 'number(s) match with fireball. You win $',ads_prize,'\n\n')
        elif(count ==2):
            z = int(0)
            while(z < len(ads_cp_user)):
                if(ads_cp_user[z] == ads_fbnum):
                    ads_prize = 100
                    break
                else:
                    z = z +1

            if(ads_prize == 100):
                print('\nPRAISE HAIL FIREBALL! You win $',ads_prize,'\n\n')
            else:
                print('\nBetter Luck Next Time!\n\n')
        else:
            print('\nBetter Luck Next Time!\n\n')
        ads_ch()

'''
______________________________________Without fireball____________________________________________
'''
def ads_p3_no_fb():
    #------------------------VARIABLES
    #input
    ads_cnum1 = input('Enter 1st lottery number: ')
    ads_cnum2 = input('Enter 2nd lottery number: ')
    ads_cnum3 = input('Enter 3rd lottery number: ')
    #Convert them to int
    ads_cnum1 = int(ads_cnum1)
    ads_cnum2 = int(ads_cnum2)
    ads_cnum3 = int(ads_cnum3)
    if((ads_cnum1 < 0 or ads_cnum1 > 9) or (ads_cnum2 < 0 or ads_cnum2 > 9) or (ads_cnum3 < 0 or ads_cnum3 > 9)):
        print('Kindly select numbers between 0 and 9\n')
        ads_p3_no_fb()
    else:
    #Initialize list
        ads_userpicks = list()
        #Add them in list
        ads_userpicks.append(ads_cnum1)
        ads_userpicks.append(ads_cnum2)
        ads_userpicks.append(ads_cnum3)
        ads_userpicks.sort()

        #----------------------- LOTTERY NUMBERS
        #Number generators
        ads_rnum1 = randint(0,3)
        ads_rnum2 = randint(3,6)
        ads_rnum3 = randint(6,9)
        #Initialize an empty list
        ads_randompicks = list()
        ads_randompicks.append(ads_rnum1)   #Edit them later
        ads_randompicks.append(ads_rnum2)
        ads_randompicks.append(ads_rnum3)
        ads_randompicks.sort()
        #---------------------------Display numbers
        print('\nUser picks: ',ads_userpicks)
        print('Lottery picks: ',ads_randompicks)

        #--------------------------Create 2 lists & Copy Elements from both lists
        ads_cp_user = list(ads_userpicks)
        ads_cp_lt = list(ads_randompicks)

        #-------------------------Using while loop to iterate through list for comparison
        # Pointer variables
        i = 0
        i = int(i)
        j = 0
        j = int(j)

        #-----Selects a user number and compares it with every element in lottery list
        while ( i < len(ads_cp_user) ):
            j = 0   #Number list pointer goes back to 0
            while (j < len(ads_cp_lt)):
                if(ads_cp_user[i] == ads_cp_lt[j]):
                    ads_cp_user[i] = 'X'    # X = Y
                    ads_cp_lt[j] = 'Y'
                    break
                else:
                    j = j + 1
            i = i+ 1
        #-----------------------------end loops


    #-----------------FINAL RESULT
        i = 0
        count = 0   # To count number of Y's in lottery
        count = int(count)
        while( i < len(ads_cp_lt)):
            if(ads_cp_lt[i] == 'Y'):
                count += 1
            i +=1

        #PRIZE ALLOCATION
        if(count == 3):
            print("\nCongratulations! You win $100\n\n " )
        else:
            print('\nBetter luck next time\n\n')

    #ads_ch()

ads_main_menu()
