#!/bin/python3

def questionnaire() :
    name = str(input("What is your name?\n")).lower()
    age = input("How old are you?\n")
    likepy = str(input("Do you like python? Yes or No.\n")).lower()
    worldflat = bool(input("The world is flat. True or False?\n"))
    comments = {}
    if name == "jake" :
        comments['name'] = "That's my name!"
    else :
        comments['name'] = "That's not my name!" 
    if int(age) < 100 and int(age) > 70 :
        comments['age'] = "You're a dinosaur"
    elif int(age) > 100 :
        comments['age'] = "You're not " + age + ". Nice try."
    if likepy == "yes" :
        comments['likepy'] = "Me too!"
    elif likepy == "no" :
        comments['likepy'] = "Sounds like a skill issue"
    if worldflat == True :
        comments['worldflat'] = "Idiot."
    else : 
        comments['worldflat'] = "I have no qualms with you."
    print("See my comments below:\n")
    return(comments)
