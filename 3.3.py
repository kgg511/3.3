
stuff = list(range(1000))
total = 0.0
index = 0
for item in stuff:
    cost = 1*(.5**stuff[index])
    index = index + 1
    total = cost + total
    print('The total is now' + str(total))

    




    
