import matplotlib.pyplot as plt

x_values = list(range(1, 5001))
y_values = [x**3 for x in x_values]

plt.scatter(x_values, y_values, c= y_values, cmap=plt.cm.YlOrRd, edgecolor='none', s=40)

# Set chart title and lable axis
plt.title("Cube Numbers 15-2", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Cube of Value", fontsize=14)

# Set the size of the tick lables
plt.tick_params(axis = 'both', which='major', labelsize=14)

plt.show()