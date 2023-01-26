##Modelling - Using software abstractions to represent a real or virtual problem.

##A model is a block of code or logic that takes in an argument or multiple arguments (inputs) and returns a set of results (outputs). Sometimes refered to as blackboxes - only care about the in/outputs not the workings. 

##Scenarios - conditions that can change

##Simulation - Running a model to allow different scenarios to be tested.

##Building a model of a thermostat 

##Input A is the live data coming in. Iput B is the temp limit/target. B could have a default setting, it can be used to simulate different scenarios. Output C is a single value - 0 or 1 for on or off.

def thermostat(actual, target):
  if actual < target:
    return 1
  else:
    return 0

tempOnOrOff = thermostat(18, 20)
print(tempOnOrOff)

##Create a test table for this model
##Actual: 15, 15, 16, 19, 0, 100
##Target: 20, 15, 15, -1, 1, -100

##This evaluates the model

##What happens if we change the default temp to 14?
##################################

import random

diceNumber = random.randint(1, 6)
print(diceNumber)

def diceRoll(actual, guess):
  if actual == guess:
    return 1
  else:
    return 0
diceGuess = int(input("Guess the number on the dice: "))

rightGuess = diceRoll(diceGuess, diceNumber)  

print(rightGuess)
##########################

## Functions with 3 arguments

def monthlyRepayment(principal, interest, years):
  finalAmount = principal *((1 + interest) ** years)
  monthlyAmount = (finalAmount/(years *12))
  return round(monthlyAmount, 2)

testCase = monthlyRepayment(10000, 0.032, 6)
print(testCase)

##Create a test table for this model
################################

##Decision making - whether a layer will play a game of tennis based on historical data. 

##The are 4 attributes based on weather - outlook, temp, huidity, wind. Depending on these weather conditions, the player eith played or didn't play. Due to 14 different outcomes its hard to plan.__doc__

##Can use a decision tree. This develops an algorithm that lets us identify al posible decision making paths. Root -> branch -> branch -> outcome. Doing this there are 5 decision making paths from 14 records.__doc__

##Using these 5 we can create our code.


def playTennis(outlook, humidity, wind):
  if outlook == "Overcast":
    return "Yes"
  elif outlook == "Sunny":
    if humidity == "High":
      return "No"
    else:
      return "Yes"
  else:
    if wind == "Strong":
      return "No"
    else:
      return "Yes"

shouldPlay = playTennis("Overcast", "High", "Weak")
print(shouldPlay)
  
