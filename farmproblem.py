#In this exercise, the challenge, is helping a farmer, who has three types of animals, and needs help in counting how many legs all the animals have
# #The farmer breeds three species:, i.e., chicken (2 legs), cows (4 legs) and pigs (4 legs)
#The farmer has counted his animals and he gives you a subtotal for each species.
# The aim is to implement a function that returns the total number of legs of all the animals.
numberOfChicken = input ("Enter number of Chickens: ")
numberOfCows = input("Enter number of Cows: ")
numberOfPigs =input("Enter number of Pigs: ")
numberOfLegs = 2*int(numberOfChicken) + 4*int(numberOfCows) + 4*int(numberOfPigs)
print("You have:\n\n" + numberOfChicken + " Chickens\n" + numberOfCows + " Cows\n" + numberOfPigs + " Pigs")
print("====================================")
print("Number of Legs is:  ", numberOfLegs)