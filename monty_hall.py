import argparse
import random

# Define the simulation parameters.
parser = argparse.ArgumentParser(description='Simulate the Monty Hall problem.')
parser.add_argument('-d', type=int, metavar='Doors', help='Number of doors.', default=3)
parser.add_argument('-n', type=int, metavar='Simulations', help='Number of simulations.', default=1000)
args = parser.parse_args()
numberOfDoors = args.d
numberOfSimulations = args.n

for isSwitchingDoor in [True, False]:
    winCount = 0
    for currentSimulation in range(0, (numberOfSimulations - 1)):
        # Generate the doors.
        correctDoor = random.randint(0, (numberOfDoors - 1))
        incorrectDoors = []
        for i in range(0, numberOfDoors):
            if i != correctDoor:
                incorrectDoors.append(i)

        # Pick a random door.
        firstGuess = random.randint(0, (numberOfDoors - 1))

        # Show a goat.
        validGoatDoors = list(incorrectDoors)
        if firstGuess in validGoatDoors:
            validGoatDoors.remove(firstGuess)
        goatDoor = random.choice(validGoatDoors)

        # If switching doors, find another valid door.
        secondGuess = -1
        if isSwitchingDoor:
            remainingDoors = []
            for i in range(0, numberOfDoors):
                if i != firstGuess and i != goatDoor:
                    remainingDoors.append(i)
            secondGuess = random.choice(remainingDoors)
        else:
            secondGuess = firstGuess

        # Evaluate the win.
        if secondGuess == correctDoor:
            winCount += 1

    # Print the score.
    winPercentage = float(winCount)/float(numberOfSimulations)
    if isSwitchingDoor:
        print("Switching doors score: " + str(winCount) + " of " + str(numberOfSimulations) + " (" + '{:.1%}'.format(winPercentage) + ")")
    else:
        print("Keeping doors score: " + str(winCount) + " of " + str(numberOfSimulations) + " (" + '{:.1%}'.format(winPercentage) + ")")
