with open("input.txt","r") as f:
    lines = f.readlines()
    f.close

lines = [i.strip().split(" ") for i in lines]
score = 0

A = dict(win = "B", lose = "C")
B = dict(win = "C", lose = "A")
C = dict(win = "A", lose = "B")
moves = {
  "A" : A,
  "B" : B,
  "C" : C
}

for round in lines:
    if round[1] == "X": ##lose
        move = moves[round[0]]["lose"]
        score += ord(move) - 64
    if round[1] == "Y": ##draw
        score += ord(round[0]) - 61
    if round[1] == "Z": ##win
        move = moves[round[0]]["win"]
        score += ord(move) - 58

print(score)
