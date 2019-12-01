
f = open("Day1input.txt", "r")
data = f.readlines()
sumOfFuel = 0

for moduleMass in data:
    # calculate fuel for module
    moduleMass = int(moduleMass)
    fuelForModule = int(moduleMass/3)-2
    sumOfFuel += fuelForModule

    # recursively calculate fuel for fuel for fuel...
    recFuel = int(fuelForModule/3)-2
    while recFuel > 0:
        sumOfFuel += recFuel
        recFuel = int(recFuel/3)-2





print(f'The elves need this much fuel: {sumOfFuel}')
f.close()