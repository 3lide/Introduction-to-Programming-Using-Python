currentPopulation = 3120324986
totalTime = 365 * 24 * 3600

for i in range(5):
    bronPopulation = totalTime // 7
    deathPopulation = totalTime // 13
    immigrantPopulation = totalTime // 45
    currentPopulation = currentPopulation + bronPopulation - \
        deathPopulation + immigrantPopulation
    print("第{0}年的人口是{1}".format(i + 1, currentPopulation))
