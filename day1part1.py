import math

### Part 1

lines = []
with open("day1part1.txt", 'r') as f:
    lines = f.readlines()

for line in lines:
    line = line.strip
size = 0
for i in range(len(lines)-1):
    if(int(lines[i+1])-int(lines[i]) > 0):
        size += 1

print("number of positive increments: {}\ntotal length: {}".format(size,len(lines))) 

### Part 2

threeSet = []

for i in range(len(lines)-2):
    threeSet.append([int(lines[i]),int(lines[i+1]),int(lines[i+2])])

secondSize = 0
for i in range(len(threeSet)-1):
    if(sum(threeSet[i+1]) > sum(threeSet[i])):
        secondSize += 1
print("number of positive tripples: {}\ntotalNumber".format(secondSize,len(threeSet)))