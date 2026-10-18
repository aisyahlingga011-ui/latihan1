for i in range(5):
    print("index:", i)

# fungsi list()
r = range(5)
print("r:", list(r))

# ke-3 perulangan ini ekuivalen
for i in range(3):
    print("index:", i)

for i in range(0, 3):
    print("index:", i)

# (dilengkapi: di PDF snippet ketiga terpotong di tepi halaman)
for i in range(0, 3, 1):
    print("index:", i)

# tambahan contoh
for i in range(2, 10, 2):
    print("index:", i)

for i in range(5, -5, -1):
    print("index:", i)