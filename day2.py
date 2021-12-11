### Part 1

lines = []
with open("day2part1.txt", "r") as f:
    lines = f.readlines() 

x = 0
y = 0

for line in lines:
    twoSet = line.split()
    if (twoSet[0] == "forward"):
        x += int(twoSet[1])
    elif (twoSet[0] == "up"):
        y -= int(twoSet[1])
    elif (twoSet[0] == "down"):
        y += int(twoSet[1])
    else:
        print("error!")

print("X: {} Y: {} X*Y: {}".format(x,y,x*y))

### Part 2
x = 0
y = 0
aim = 0
for line in lines:
    twoSet = line.split()
    if (twoSet[0] == "forward"):
        x += int(twoSet[1])
        y += aim*int(twoSet[1])
    elif (twoSet[0] == "up"):
        # y -= int(twoSet[1])
        aim -= int(twoSet[1])
    elif (twoSet[0] == "down"):
        # y += int(twoSet[1])
        aim += int(twoSet[1])
    else:
        print("error!")


print("X: {} Y: {} aim: {} X*Y: {}".format(x,y,aim,x*y))