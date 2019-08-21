print('number\tsquera')
print('--------------')
for i in range(0,11):
    squera=i**2
    print(i ,'\t\t', squera)
while True:
    start = int(input('please enter your start: '))
    end = int(input('please enter your end: '))
    print('number\tsquera')
    print('--------------')
    if start < end:
        for number in range(start, end + 1):
            squer = number ** 2
            print(number, '\t\t', squer)
    elif end<start:
        for number in range(end, start+1):
            squer = number ** 2
            print(number, '\t\t', squer)


