Tralalero = [
    ["x", "o", "x"],
    ["o", "x", "x"],
    ["x", "o", "x"]
]

for i in range(3):
    print(Tralalero[i], "!", Tralalero[i+1], "!",Tralalero[i+2])
    if i < 2:
        print("===+===+===")