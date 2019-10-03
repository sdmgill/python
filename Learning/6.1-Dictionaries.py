# a Python dictionary is a collection of key-value pairs
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])


new_points = alien_0['points']
print("You just earned " + str(new_points) + " points")

print(alien_0)

#add new key-value pairs
print('\n"Adding new key-pair values to existing dictionary"')
alien_0['x_position']=0
alien_0['y_position']=25
print(alien_0)

#modify a pair
print('\n"Modifying a pair"')
print("The alien is " + alien_0['color'] + ".")

alien_0 = {'color':'yellow'}
print("The alien is now " + alien_0['color'] + ".")

#More complex example
print('\n"More complex example"')
alien_0	= {'x_position':0,'y_position':25,'speed':'medium'}
print("Original x-position: " +str(alien_0['x_position']))

# Move alien to the right.
# Determine how far to move the alien based on its current speed
if alien_0['speed'] =='slow':
	x_increment = 1
elif alien_0['speed'] =='medium':
	x_increment = 2
else:
	x_increment = 3
	
# The new position is the old position plus the increment
alien_0['x_position'] = alien_0['x_position'] + x_increment

print("New x-position: " +str(alien_0['x_position']))

#change it to 'fast'
print('\n"Change speed to fast"')
alien_0['speed']='fast'

if alien_0['speed'] =='slow':
	x_increment = 1
elif alien_0['speed'] =='medium':
	x_increment = 2
else:
	x_increment = 3
	
# The new position is the old position plus the increment
print('\n"Note how the new position is now 5. 0+2 for the first run, then 2+3 for the next"')
print("Original x-position: " +str(alien_0['x_position']))
alien_0['x_position'] = alien_0['x_position'] + x_increment

print("New x-position: " +str(alien_0['x_position']))

#Removing key-value pairs
print('\n"Removing key-value pairs"')
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

del alien_0['points']
print(alien_0)

