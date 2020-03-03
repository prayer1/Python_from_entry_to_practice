motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

motorcycles.append('ggogo')
print(motorcycles)

arr = [];
arr.append('first')
arr.append('second')
arr.append('third')
print(arr)
arr.insert(0, 'me')
print(arr)

del(arr[0])
print(arr)

pop_arr = arr.pop()
print(pop_arr)
print(arr)