# %% Mengakses elemen set
fellowship = {'aragorn', 'gimli', 'legolas'}

for p in fellowship:
    print(p)

# %% Eliminasi elemen duplikat - 1
data = {1, 2, 3, 2, 1, 4, 5, 2, 3, 5}
print(data)

# %% Eliminasi elemen duplikat - 2
data = [1, 2, 3, 2, 1, 4, 5, 2, 3, 5]
print(data)

data_unique_set = set(data)
print(data_unique_set)

data_unique = list(data_unique_set)
print(data_unique)

# %% Mengecek apakah element ada
fellowship = {'aragorn', 'gimli', 'legolas'}
to_find = 'gimli'

if to_find in fellowship:
    print(to_find, 'is exists within fellowship')