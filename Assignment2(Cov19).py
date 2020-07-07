# Write your Python codes on any IDE, push it up to your GitHub repository 
# and submit your GitHub Page link address in addition to your code as a plain text.
# Problem :
# Task : Estimating the risk of death from coronavirus. Write a program that;
# Takes "Yes" or "No" from the user as an answer to the following questions :
# Are you a cigarette addict older than 75 years old? Variable → age
# Do you have a severe chronic disease? Variable → chronic
# Is your immune system too weak? Variable → immune
# Set a logical algorithm using boolean logic operators (and/or) and 
# use if-statements with the given variables 
# in order to print out us a message : "You are in risky group"(if True ) or 
# "You are not in risky group" (if False).

age = input('Are you a cigarette addict older than 75 years old? ').lower()
chronic = input('Do you have a severe chronic disease? ').lower()
immune = input('Is your immune system too weak? ').lower()
if age == 'yes':
    age = True
else:
    age == False

if chronic == 'yes':
    chronic = True
else:
    chronic = False

if immune == 'yes':
    immune = True
else:
    immune = False

risk = (age or chronic or immune)

if risk == True:
    print("You are in risky group")
else:
    print("You are not in risky group")
