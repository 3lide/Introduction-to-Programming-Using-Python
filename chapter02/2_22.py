numberOfYears = eval(input("Enter the number of years: "))
currentPopulation = 3120324986
totalTime = 365 * 24 * 3600

for i in range(numberOfYears):
    bronPopulation = totalTime // 7
    deathPopulation = totalTime // 13
    immigrantPopulation = totalTime // 45
    currentPopulation = currentPopulation + bronPopulation - \
        deathPopulation + immigrantPopulation

print("The population in {} years is {}.".format(numberOfYears, currentPopulation))