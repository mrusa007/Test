import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([1, 2, 3, 4, 5])
ypoints = np.array([3, 8, 1, 10, 5])

#PLot line with markes
plt.plot(xpoints, ypoints, marker='o')

#add labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Line Plot with Markers')
#pip
plt.show()