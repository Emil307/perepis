firstCount = 0
secondCount = 0
thirdCount = 0
days = []
pointM = 0
dateWay = 0
startPoints = []
finishPoints = []
f = open('travels.txt', 'r')
for line in f:
    data = line.split()
    day = int(data[0])
    start = data[2]
    finish = data[3]
    mass = int(data[6])
    way = int(data[4])
    if start == 'Липки':
        pointM += mass
    if day not in days:
        days.append(day)
    for i in range(len(days)):
        print(days[i])
    if day == 1:
        firstCount += 1
        dateWay += way
    elif day == 2:
        secondCount += 1
    elif day == 3:
        thirdCount += 1
    if start not in startPoints:
        startPoints.append(start)
    if finish not in finishPoints:
        finishPoints.append(finish)
#print(pointM)
#print(dateWay)
#print(len(startPoints), startPoints)
#print(len(finishPoints), finishPoints)
#print(days)
