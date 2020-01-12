#!/usr/bin/python

def isOneBitCharacter(bits):
    """
    :type bits: List[int]
    :rtype: bool
    """
    if bits[-1] != 0:
        return False

    jump = False

    for i in xrange(0, len(bits)):
        if jump == True:
            if i == len(bits) - 1:
                return False

            jump = False
            continue

        if bits[i] == 1:
            jump = True

    return True   

print isOneBitCharacter([1,0,0])
print isOneBitCharacter([1,0,1,0])
print isOneBitCharacter([1,0,1,1])
print isOneBitCharacter([1,0,1,0,0])
print isOneBitCharacter([1,0,1,0,0,0])
