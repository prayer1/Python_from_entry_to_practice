alien_0 = {'x_position': 1, 'y_position': 25, 'speed': 'fast'}
print("Original x-position:" + str(alien_0['x_position']))

#想右移动外星人
#根据外星人当前速度决定其移动多远
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

#新位置等于老位置加增量
alien_0['x_position'] = alien_0['x_position'] + x_increment
print("New x-position:" + str(alien_0['x_position']))