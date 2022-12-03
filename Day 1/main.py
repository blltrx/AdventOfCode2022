with open("input.txt","r") as f: #open input
    lines = f.readlines()
    f.close()

elves = lines.count("\n") #create 2d array of all elves inventory
l = [[] for i in range(elves+1)]
elf = 0
for line in lines:
    if line == "\n":
        elf += 1 
    else:
        l[elf].append(line.replace("\n",""))

t = [] #stores totals for each inventory

for i in l: #calculate total for each
    sum = 0
    for item in i:
        sum += int(item)
    t.append(sum)

t.sort()
print(t[-1]) #part a
print(t[-1]+t[-2]+t[-3]) #part b