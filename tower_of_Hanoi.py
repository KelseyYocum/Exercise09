
#towers of Hanoi
t1 = [5,4,3,2,1]
t2 = []
t3 = []


def move_rings(n, start, target, temp):
    # n is number of rings
    # start is starting tower
    #target is ending tower
    #temp is the buffer

    if n == 1:
        target.append(start.pop())
    else:
        move_rings(n-1, start,temp, target)
        target.append(start.pop())
        move_rings(n -1,temp,target,start)



def print_towers():
    print t1
    print t2
    print t3


move_rings(5, t1, t2, t3)
print_towers()
