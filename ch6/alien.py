alien_0 = {'color':'green', 'point':5}
print(alien_0['color'])
print(alien_0['point'])

alien_0['x_position'] = 0
alien_0['y_position'] = 1
print(alien_0)

alien_0['color'] = 'red'
print(alien_0)

del alien_0['color']
print(alien_0)