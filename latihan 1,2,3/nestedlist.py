matrix = [
    [0, 1, 0, 1, 0],
    [1, 1, 1, 0, 0],
    [0, 0, 0, 1, 1],
    [0, 1, 1, 1, 0],
]
for row in matrix:
    for cell in row:
        print(cell, end=" ")  # (dikoreksi: di PDF tertulis "cel", jadi akan error)
    print()