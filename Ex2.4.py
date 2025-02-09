import numpy as np

A1 = np.array([[1,2],[3,4]])
A2 = np.array([[11,12],[13,14]])

print("Vertically Stacked:\n",np.vstack((A1,A2)))
print("Horizontally Stacked:\n",np.hstack((A1,A2)))