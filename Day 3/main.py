with open("input.txt","r") as f:
    read = f.readlines()
    f.close
lines = [i.strip() for i in read]
for index, line in enumerate(lines):
    lines[index] = [line[:int(len(line)/2)], line[int(len(line)/2):]]
total = 0

for line in lines:
    match = ""
    for char in line[0]:
        if char in line[1]:
            if char.isupper(): total += ord(char) - 38
            if char.islower(): total += ord(char) - 96
            break

print(total) #part a

lines = [i.strip() for i in read]
total = 0
threes = []
for count in range(0,int(len(lines)),3):
    threes.append(lines[count:count+3])

for three in threes:
    for char in three[0]:
        if char in three[1] and char in three[2]:
            if char.isupper(): total += ord(char) - 38
            if char.islower(): total += ord(char) - 96
            break
    
print(total) #partb
