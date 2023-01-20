count = 0
sinceYear = int(input())
forYear = int(input())
f = open('Perepis.txt', 'r')
for line in f:
    data = line
    data = data.split()
    year = int(data[3].split('.')[2])
    if year < 1978:
        count += 1
        print('фамилия:', data[0])
    if sinceYear <= year and year <= forYear:
        print(data[:2])
        print(year)
print(count)

