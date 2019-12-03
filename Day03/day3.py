# Generate a Grid with dimensions: 
x_size = 25000
y_size = 16000
grid = [[0] * y_size for i in range(x_size)]


intersectionList = []
shortestDistance = 999999

# Read in Instructions
f = open("Day3input.txt")
line1Instructions = f.readline().split(',')
line2Instructions = f.readline().split(',')

x_pointer = 21605
y_pointer = 3735

def setPointers():
    global x_pointer, y_pointer
    x_pointer = 21605
    y_pointer = 3735

def goRight(steps: int, lineNo: int):
    global x_pointer, y_pointer
    for i in range(steps):
        x_pointer +=1
        grid[x_pointer][y_pointer] += lineNo
        checkForIntersection()

def goLeft(steps: int, lineNo: int):
    global x_pointer, y_pointer
    for i in range(steps):
        x_pointer -=1
        grid[x_pointer][y_pointer] += lineNo
        checkForIntersection()

def goUp(steps: int, lineNo: int):
    global x_pointer, y_pointer 
    for i in range(steps):
        y_pointer +=1
        try:
            grid[x_pointer][y_pointer] += lineNo
        except IndexError:
            print(x_pointer, y_pointer)
            exit(1)

        checkForIntersection()
        

def goDown(steps: int, lineNo: int):
    global x_pointer, y_pointer
    for i in range(steps):
        y_pointer -=1
        grid[x_pointer][y_pointer] += lineNo
        checkForIntersection()

def checkForIntersection():
    global x_pointer, y_pointer, grid, intersectionList
    if grid[x_pointer][y_pointer] == 3:
        intersectionList.append((x_pointer, y_pointer))
        # print(grid[x_pointer][y_pointer], x_pointer, y_pointer)

def execInstructions(instructions, lineNo: int):
    global x_pointer, y_pointer
    for inst in instructions:
        if inst.startswith("R"):
            goRight(int(inst[1:]), lineNo)
        elif inst.startswith("L"):
            goLeft(int(inst[1:]), lineNo)
        elif inst.startswith("U"):
            goUp(int(inst[1:]), lineNo)
        elif inst.startswith("D"):
            goDown(int(inst[1:]), lineNo)
        else:
            print("Life is misery.")
            exit(1)

def manhattenForumla(x_coord: int, y_coord: int):
    global shortestDistance
    mDistance = abs(x_coord-x_pointer)+abs(y_coord-y_pointer)
    if mDistance < shortestDistance and mDistance != 0:
        shortestDistance = mDistance

# The Actual Script
execInstructions(line1Instructions, 1)
setPointers()
execInstructions(line2Instructions, 2)
setPointers()
for inter in intersectionList:
    manhattenForumla(inter[0], inter[1])

print(f"Found {len(intersectionList)} crossings.")

print(f"The shortest distance from the central point is: {shortestDistance}")

'''for x in grid:
    print(' '.join(str(y) for y in x))'''

