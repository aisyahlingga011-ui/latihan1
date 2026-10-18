# operator assignment
num_1 = 12
num_2 = 24
num_2 = 12
# (dilengkapi: di PDF baris ini terpotong, hanya tertulis `num_1 + num_2`)
num_3 = num_1 + num_2

# operator logika
res = (4 == 5) and (2 != 3)
res = (4 == 5) or (2 != 3)
res = not (2 == 3)

# operator is
num_1 = 100001
num_2 = 100001
res = num_1 is num_2
print("num_1 is num_2 =", res)
print("id(num_1): %s, id(num_2): %s" % (id(num_1), id(num_2)))

# print() dengan beberapa argumen
print("message: %s %s %s" % ("hello", "python", "learner"))
print("message:", "hello", "python", "learner")

# fungsi id()
data_1 = "hello world"
id_data_1 = id(data_1)
print("data_1:", data_1)
# output ➜ data_1: hello world
print("id_data_1:", id_data_1)
# output ➜ id_data_1: 19441xxxxxxxx