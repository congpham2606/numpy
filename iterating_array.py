import numpy as np

arr = np.array([1, 2, 3])

for x in arr:
    print(x)
arr = np.array([[1, 2, 3], [4, 5, 6]])

for x in arr:
    print(x)
for x in arr:
    for y in x:
        print(y)
'''sử dụng nditer()'''
arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
for x in np.nditer(arr[0:1,::,0:1]):
    print(x)
arr = np.array([1, 2, 3])

for x in np.nditer(arr, flags=['buffered'], op_dtypes=['S']):
    print(x) 