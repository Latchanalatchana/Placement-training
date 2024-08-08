import numpy as np

arr = np.array([5, 12, 7, 18, 3])
arr[arr > 10] = 0
print("Array after replacing elements greater than 10:", arr)
