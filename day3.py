### Part 1
lines = []
with open("day3.txt","r") as f:
    lines = f.readlines();

msb = [0,0,0,0,0]
lsb = [0,0,0,0,0]
for line in lines:
    for i in range(5):
        if (line[i] == "1"):
            msb[i] += 1
        elif(line[i] == '0'):
            lsb[i] += 1
print(msb,"\n",lsb)

gamma = ""
epsilon = ""
for i in range(5):
    if (msb[i] > lsb[i]):
        gamma += "1"
        epsilon += "0"
    else:
        gamma += "0"
        epsilon += "1"


print(gamma,"\n",epsilon)










### Part 2