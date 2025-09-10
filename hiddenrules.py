#All functions return 3 items, last player's position, new player's position and new position of the destination

#prime number rule
def hrule1(lastPos, newPos, destPos, mapSize):
    primeNum = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    if newPos in primeNum and newPos > mapSize:
        print("Prime number rule activated! Moving back one row.")
        return lastPos, newPos - mapSize, destPos
    return lastPos, newPos, destPos

#multiple of 11 rule
def hrule2(lastPos, newPos, destPos, mapSize):
    if newPos % 11 == 0 and newPos != 0:
        print("Multiple of 11 rule activated! Destination moving left.")
        return lastPos, newPos, destPos - max(destPos%mapSize - 1, 0)
    return lastPos, newPos, destPos

#multiple of 6 rule
def hrule3(lastPos, newPos, destPos, mapSize):
    if lastPos % 6 == 0 and newPos - lastPos == mapSize and lastPos != 0:
        print("Multiple of 6 rule activated! Moving back to last position.")
        return lastPos, lastPos, destPos
    return lastPos, newPos, destPos

#multiple of 4 rule
def hrule4(lastPos, newPos, destPos, mapSize):
    if newPos % 4 == 0 and newPos != 0:
        print("Multiple of 4 rule activated! Moving back 4 spaces.")
        return lastPos, newPos - 4, destPos
    return lastPos, newPos, destPos

#function to check all rules
def checkRules(lastPos, newPos, destPos, mapSize):
    rules = [hrule1, hrule2, hrule3, hrule4]

    lastPos, newPos, destPos = hrule1(lastPos, newPos, destPos, mapSize)
    lastPos, newPos, destPos = hrule2(lastPos, newPos, destPos, mapSize)
    lastPos, newPos, destPos = hrule3(lastPos, newPos, destPos, mapSize)
    lastPos, newPos, destPos = hrule4(lastPos, newPos, destPos, mapSize)

    return lastPos, newPos, destPos