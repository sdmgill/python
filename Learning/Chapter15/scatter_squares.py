import matplotlib.pyplot as plt


x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]
"""
flow during exercises:
#1 plt.scatter(2, 4)
#2 plt.scatter(2, 4, 2=200)
#3  x_values = [1, 2, 3, 4, 5]
    y_values = [1, 4, 9, 16, 25]
    plt.scatter(x_values, y_values, s=100)
#4  x_values = list(range(1, 1001))
    y_values = [x**2 for x in x_values]
    plt.scatter(x_values, y_values, s=40)
#5  same x and y for the rest
    remove blacklines from lines
    plt.scatter(x_values, y_values, edgecolor='none', s=40)  
#6  change line to red
    plt.scatter(x_values, y_values, c='red', edgecolor='none', s=40)
#7  change line color using RGB settings (0-1 for each) 0 = darker, 1 = lighter    
    plt.scatter(x_values, y_values, c=(0, 0, 0.8), edgecolor='none', s=40)
#8  change color using Colormap (pyplot has several) -- color goes from light to dark 
    plt.scatter(x_values, y_values, c= y_values, cmap=plt.cm.Reds, edgecolor='none', s=40)   
"""
plt.scatter(x_values, y_values, c= y_values, cmap=plt.cm.Reds, edgecolor='none', s=40)

# Set chart title and lable axis
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# Set the size of the tick lables
plt.tick_params(axis = 'both', which='major', labelsize=14)

# Set the range for each axis
plt.axis([0, 1100, 1, 1100000])

plt.show()
# To save use
"""
plt.savefig('square_plot.jpg',bbox_inches='tight') # bbox option trims whitespace from plot. it is optional.
"""
