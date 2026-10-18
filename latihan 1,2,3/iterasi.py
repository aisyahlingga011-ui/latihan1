# list
messages = ["morning", "afternoon", "evening"]
for m in messages:
    print(m)

# tuple
numbers = ("twenty four", 24)
for n in numbers:
    print(n)

# string
for char in "hello python":
    print(char)

# dictionary
bio = {
    "name": "toyota camry",
    "year": 1993,
}
for key in bio:
    print("key:", key, "value:", bio[key])

# set
numbers = {"twenty four", 24}
for n in numbers:
    print(n)

# perulangan bersarang, pola bintang
max = int(input("jumlah bintang: "))
for i in range(max):
    for j in range(0, max - i):
        print("*", end=" ")
    print()