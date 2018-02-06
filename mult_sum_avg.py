# multiples part 1
def multiples(number):
    for var in range(0, number):
        if var % 2 == 1:
            print var
multiples(1000)

# multiples part 2
def multiples_2(number):
    for var in range(0, number+1):
        if var % 5 == 0:
            print var
multiples_2(1000000)

# sum list
def sum(aList):
    x = 0
    for val in aList:
        x += val
        print x
sum([1, 2, 5, 10, 255, 3])

# average list
def average_list(aList):
    x = 0
    for val in aList:
        x += val
    x = x/len(aList)
    print x
average_list([1, 2, 5, 10, 255, 3])