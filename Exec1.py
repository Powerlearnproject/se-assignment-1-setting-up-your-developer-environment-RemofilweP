import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

#Creating a figure and a 3D Axes
fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')

#Generating data for plotting
x = np.linespace(-5,5,100)
y = np.linespace(-5,5,100)

x,y = np.meshgrid(x,y)

z = np.sin(np.sqrt(x**2 + y**2))

#Plotting the surfaces
ax.plot_surface(x,y,z, cmap='virdis') 

#Set labels
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")

#Show Plot
plt.show()
