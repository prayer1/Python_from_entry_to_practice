friends = ['zengxiaohan', 'huangxianglin', 'zhushengquan']
print(friends)
print(friends[2] + 'can not go to the party!')

friends[2] = 'xuyangxinlei'
print(friends)

friends.insert(0, 'zhanglungui')
friends.insert(2, 'gogo')
friends.append('end')
print(friends)

name1 = friends.pop()
name2 = friends.pop()
name3 = friends.pop()
name4 = friends.pop()
print(friends)
del friends[0]
del friends[0]
print(friends)