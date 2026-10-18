list_1 = [10, 70, 20]

# cara 1
for e in list_1:
    print("elem:", e)

# cara 2
for i in range(0, len(list_1)):
    print("index:", i, "elem:", list_1[i])

# cara 3
for i, v in enumerate(list_1):
    print("index:", i, "elem:", v)