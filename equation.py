import numpy as np
import matplotlib.pyplot as plt

# Data points
x = [-40, -20, 0, 20, 40, 60, 80]
y = [61, 177.33, 296.33, 680.33, 651, 534.67, 24.67]

# Get Polynomial Regression and Graph
eq = np.poly1d(np.polyfit(x, y, 3))
print('Equation: ' + str(eq))
xRange = np.arange(-40, 80)
yReg = np.polyval(np.polyfit(x, y, 3), xRange)
plt.plot(x, y, label='Points')
plt.plot(xRange, yReg, label='Regression')

# Input Angle Calculation
inputAng = input('Enter an integer angle or type g to go to the graph: ')
# while not inputAng.isdigit():
    # if inputAng == 'g':
        # break
    # print('Try again. ', end='')
    # inputAng = input('Enter an integer angle or type g to go to the graph: ')
while not inputAng == 'g':
    print('Distance: ' + str(eq(int(inputAng))) + ' inches')
    inputAng = input('Enter an integer angle or type g to go to the graph: ')
    # while not inputAng.isdigit():
        # if inputAng == 'g':
            # break
        # print('Try again. ', end='')
        # inputAng = input('Enter an integer angle or type g to go to the graph: ')

# Graph draw
plt.show()