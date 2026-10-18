# range ke list
range_1 = range(0, 10)
list_1 = list(range_1)
print(list_1)
# output ➜ [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

range_2 = range(0, 22, 3)
list_2 = list(range_2)
print(list_2)
# output ➜ [0, 3, 6, 9, 12, 15, 18, 21]

range_3 = range(100, 0, -10)
list_3 = list(range_3)
print(list_3)
# output ➜ [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]

# string ke list
alphabets = list('abcdefgh')
print(alphabets)
# output ➜ ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

# tuple ke list
tuple_1 = (1, 2, 3, 4)
numbers = list(tuple_1)
print(numbers)
# output ➜ [1, 2, 3, 4]