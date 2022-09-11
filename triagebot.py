#Title : TriageBot
#This is a program which will triage patients based on severity of their illness
#In the Emergency Room, the concept of triage is to quickly assess a patient
#to determine 1 of 2 scenarios. Either:
    #A: the patient is medically unstable enough to require a room immediately
    #B: the patient is medically stable enough to wait to be seen 

#As there are seemingly infinite symptoms and combinations of symptoms, this program will
#naturally face some constraints, it will only perform triage based on the classic 3 
#highest priority systems in emergency medicine:
    #1: Airway
    #2: Breathing
    #3: Circulation

#TriageBot will ask user input on which body system is experiencing an issue
#TriageBot will use patient vital signs as an objective parameter to measure severity 
#TriageBot will generate vital signs, check them against conditionals, and output whether
#the patient is medically stable or unstable and categorize them accordingly. 

#due to the nature of laypeople's knowledge on vital signs and overall clinical presentation,
#the program must generate these itself and run them against conditionals which are hard-coded
#with critical values by myself. The program will not allow for vitals incompatible with life (ie; oxygen level of 20%)
#In future versions, it will be re-designed to ask user to 
#check own vital signs and input values. This mimics real-world application where medical
#staff check vital signs on a patient which they have no control over so random generation is applicable here. 

#import random as random number generation is required for vital signs
#create functions to print appropriate script for medical stability instead of repeating code
#create 3 functions for airway, breathing, and circulation which are called within initial loop
#ask for user input on which system has an issue: airway, breathing, circulation, or other
#if other: classify them as stable and end program


#if airway: call the airway function which will: 
    #ask for input on whether patient is choking, if yes - exit loop and classify as unstable. if no, 
    #generate vital signs consistent with airway issues
#if breathing: call the airway function which will:
    #ask if patient has shortness of breath or wheezing, if yes - exit loop and classify as unstable. if no,
    #generate vital signs consistent with breathing issues 
#if circulation: call the circulation function which will:
    #ask for input on whether patient is currently bleeding, pale, or dizzy - if yes, exit loop and classify unstable
    #if no, generate vitals signs consistent with circulation issues. 

import random

#functions to print the appropriate script on medical stability 
def stable():
    print('You are medically stable. Please have a seat in the lobby until we have a room for you. ')

def unstable():
    print('You are not medically stable. Please follow me to a patient room immediately.')

#functions for each choice
def airway():
    airwayStatus = input('Are you currently choking? Yes or No:\n')
    if airwayStatus == 'Yes':
        unstable()
    else:
        #generate vital signs consistent with either low or normal oxygen
        oxygen = random.randint(70, 100) #this program will not handle vitals incompatible with life, bottom range is 70
        print(f'Your oxygen level is {oxygen}%.\n')
        if oxygen <= 89:
            unstable()
        else:
            stable()

def breathing():
    breathingStatus = input('Are you wheezing or experiencing shortness of breath? Yes or No:\n')
    if breathingStatus =='Yes':
        unstable()
    else:
        #generate vital signs consistent with low or normal oxygen
        oxygen = random.randint(70, 100)
        #generate vital signs consistent with too slow or too fast breathing (normal breathing range is 12-20, program will not
        #deal with vitals incompatible with life, bottom range is 8, top is 40)
        print(f'Your oxygen level is {oxygen}%.\n')
        breaths = random.randint(8, 40)
        print(f'You are breathing {breaths} times per minute.\n')
        if oxygen <= 89 or breaths <12 or breaths >20: 
            unstable()

def circulation():
    circulationStatus = input('Are you currently bleeding, pale, dizzy, or having chest pain? Yes or No:\n')
    if circulationStatus == 'Yes':
        unstable()
    else:
        systolicPressure = random.randint(50, 200)
        diastolicPressure = random.randint(30, 100)
        print(f'Your Blood Pressure is {systolicPressure} / {diastolicPressure}.\n')
        if systolicPressure >=90 and diastolicPressure >=50:
            stable()
        else:
            unstable()

#define the function for the main program of TriageBot       

def symptomCheck ():
    symptoms = input('Welcome to TriageBot. What symptoms are you having today? Airway, Breathing, Circulation, or Other?\n')
    if symptoms == 'Other':
        stable() #calls the stable function to print script instead of using repetitious code
    elif symptoms == 'Airway':
        airway() #calls the airway function to determine airway status
    elif symptoms == 'Breathing':
        breathing() #calls the breathing function to determine breathing status
    elif symptoms == 'Circulation':
        circulation() #calls the circulation function to determine circulation status
    else:
        print('Please enter one of the four categories above to use TriageBot') 
        symptomCheck()
        #sentinel to end if input is invalid and then re-initiate the symptomCheck function

symptomCheck()


