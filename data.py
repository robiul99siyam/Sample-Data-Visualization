import matplotlib.pyplot as plt
import numpy as np


""" 
    first code run the data visialization normal 
    xpoints = np.array([0,6])
    ypoints = np.array([0,250])

"""


"""

add the linestyle 
xpoints = np.array([0,10])
ypoints = np.array([3,8,1,10])
plt.plot(ypoints,lineStyle="dashdot",marker='_')



"""

"""


xpoints = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
ypoints = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
plt.plot(xpoints,ypoints,'o')
plt.title("Sports Watch Data",loc='left')
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")
plt.grid(color = 'green', linestyle = '--', linewidth = 0.5)


"""



# pie charts make 

ypoints = np.array([50,35,50,60])
mylabels = ['Apple','Orange','Mango','Banana']
myexplode = [0.2, 0, 0, 0]
plt.pie(ypoints,labels=mylabels,explode = myexplode)
plt.show()