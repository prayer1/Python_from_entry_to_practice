magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)


for value in range(1, 5):
    print(value)


numbers = list(range(1, 7))
print(numbers)

even_numbers = list(range(2, 22, 2))
print(even_numbers)

squares = []
for value in range(1, 5):
    squares.append(value**2)
print(squares)

squares2 = [value**2 for value in range(1, 11)]
print(squares2)

players = ['a', 'b', 'c', 'd']
print(players[0:3])
print(players[-3:])

my_foods = ['apple', 'egg', 'dog']
your_foods = my_foods[:]
print(my_foods)
print(your_foods)

my_foods.append('a')
your_foods.append('b')
print(my_foods)
print(your_foods)

a_arr = ['1', '2', '3']
b_arr = a_arr
a_arr.append('a')
b_arr.append('b')
print(a_arr)
print(b_arr)