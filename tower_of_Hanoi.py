
#towers of Hanoi

def move_rings(n, start, end, temp):
    # n is number of rings
    # start is starting tower
    #end is ending tower
    #temp is the third (middle) tower

    if n == 0:
        return []
    start = range(n)
    start.reverse()

    biggest = start.pop(0)
    end.append(biggest)
   # move_rings(n-1, start, temp, end)

    print "start",start
    print "end", end
    print "temp",temp
    

    return move_rings(n-1, temp, end, start)


move_rings(5, [],[],[])