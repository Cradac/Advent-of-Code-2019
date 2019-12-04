LOWER_BOUND = 264360
UPPER_BOUND = 746325

pwd_list = []

def checkCriteria():
    pass

def hasAdjacentDoubleDigit(number: int):
    nString = str(number)
    niceCounter = 0
    flag = False
    for i in range(0,5):
        if nString[i] == nString[i+1]:
            flag = True
            try:
                if nString[i] == nString[i+2]:
                    flag = False
            except IndexError:
                pass
            try:
                if nString[i] == nString[i-1]:
                    flag = False
            except IndexError:
                pass
            if flag:
                niceCounter += 1
                flag = False
    return niceCounter > 0

def doesntDecrease(number: int):
    nString = str(number)
    for i in range(0,5):
        if int(nString[i]) <= int(nString[i+1]):
            pass
        else:
            return False
    return True

for number in range(LOWER_BOUND, UPPER_BOUND):
    if hasAdjacentDoubleDigit(number) and doesntDecrease(number):
        pwd_list.append(number)

print(f"There are {len(pwd_list)} possible passwords.")

'''
log = open("log.log", "w+")
log.write("\n".join(list(map(str, pwd_list))))
log.close()
'''     