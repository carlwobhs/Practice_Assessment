'''
    author: Mr Wright
    date: 20/08/2025
    version: 1
    description: Heads and tails program - demonstating commenting.
'''
#--------------libaries------------------------------
import random  #use randint to get random numbers or choice to select from list

#--------------functions-----------------------------
#-------------------------------------
# This function get a random number to 
# choose from a list of heads or tails like a coin flip.
#-------------------------------------
def heads_tails():
    print("Testing it worked")

#---------------main routine-------------------------
valid = True #looping my validation 
print('Welcome to Heads and Tails game') #greeting
name = input('Enter your name: ')

#validating the users input for age
while(valid):
    try:
        age = int(input('Enter your age: ')) #changing string input to integer 1-18    1 and 18 plus test 0 and 19
    except:
        print('You did not enter a valid number')
        continue

    if(age >= 12 and age <= 65): #range check for merit
        if(age == None or not age.isdecimal()):
        #valid = False
            break #jumping statement leaves the loop
    else:
        print('You entered an age out of range from 12-65')

heads_tails() #calling a function with no parameter