import numpy as np
arr= np.array([1,2,3,4,5,6,7])
print(arr[1:5])
print(arr[4:])
print(arr[:4])
'''negative slicing'''
print(arr[-3:-1])
'''step'''
print(arr[1:5:2])
'''slicing mảng 2 chiều'''
arr2 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(arr2[1, 1:4])
print(arr2[0:2, 2])
print(arr2[0:2, 1:4])