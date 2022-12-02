with open("input.txt","r") as f:
    lines = f.readlines()
    f.close

lines = [i.strip() for i in lines]

score = 0
print(lines)

for round in lines:
    if round[0] == "A":
        if round[2] == "X": score += 4
        if round[2] == "Y": score += 8
        if round[2] == "Z": score += 3
    if round[0] == "B":
        if round[2] == "X": score += 1
        if round[2] == "Y": score += 5
        if round[2] == "Z": score += 9
    if round[0] == "C":
        if round[2] == "X": score += 7
        if round[2] == "Y": score += 2
        if round[2] == "Z": score += 6

print(score)

