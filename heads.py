'''
    author: Mr Wright
    date: 22/08/25
    version: 1
    description: Practice assessment task
'''
#---------libraries-------------------------------------
import random 

#--------functions--------------------------------------

#------------------------------------------
# This function gets no paramenters.
# It plays a game by flipping a random number.
#------------------------------------------
def heads_tails():
    print('It works')
    pass

#------------------------------------------
# Introduces the game... 
# And greets the user by their name
#------------------------------------------
def intro(name):
    print(f'Welcome to my Heads and Tails game {name}') #adding the name to the message

#--------main routine-----------------------------------
valid = True
age = 0


name = input('Enter your name: ') #get user name
if(len(name)>= 2 and len(name) <= 10): #merit boundaries. 4 to check..
    print("Valid name entered.")

while(valid):
    try:
        age = int(input('Enter your age: ')) #get users age
    except:
        print('There was an error with your age input')

    if(age >= 12 and age <= 18): #merit checking - boundary/range checking.
        if(not age == None or not str(age).isdecimal()): #checking for invalids
            print("The age entered is fine.") 
            #valid = False 
            break #jump out the loop its in ... jumping statement
    else:
        print("Your age was not between 12-18")

# we don't want it to carry on the program with the wrong data entered


intro(name) #this function introduces the game passing name as a paramenter
heads_tails() #calling function with string name parameters