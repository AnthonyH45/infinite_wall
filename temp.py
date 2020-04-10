def find_door(wall):
    found_door = False
    pos = int(len(wall)/2) # assume wall is even length
    print("Starting at index", pos)
    sum = 0
    offset = 1

    while found_door == False:
        print("\noffset=",offset,"total steps=",sum)
        # this is just so we dont break our program when running
        if pos+offset > len(wall) or pos-offset < 0:
            offset = len(wall)

        for i in range(1,offset+1):
            print("\tchecking pos+i",(pos+i)) #,"| pos-i",(pos-i))
            if wall[int(pos+i)] == 1: # or wall[int(pos-i)] == 1: # found door 
                found_door = True
                print("\tFOUND DOOR")
                sum += i
                return sum

        # we have to add 2*offset, as we walk
        # offset distance away, and then have to
        # walk the same distance coming back
        sum += (2*offset)
        print("")

        for i in range(1,offset+1):
            print("\tchecking pos-i",(pos-i)) #,"| pos-i",(pos-i))
            if wall[int(pos-i)] == 1: # or wall[int(pos-i)] == 1: # found door 
                found_door = True
                print("\tFOUND DOOR")
                sum += i
                return sum

        sum += (2*offset)
        if offset == 0:
            offset = 1
        else:
            offset *= 2
        print("\twe walked a total of",sum,"steps this offset",int(offset/2))

    return sum

def main():
    wall = []
    door = 40
    for x in range(0,100):
        wall.append(0)
    print("wall is ",len(wall), "steps long\nDoor is located at wall[",door,"]")
    wall[door] = 1
    print("\ntotal steps=",find_door(wall))

main()
