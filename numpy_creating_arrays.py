import numpy as np
arr=np.array([1,2,3,4,5])
print(arr)
print(type(arr))
arr1=np.array((1,2,3,4,5))
'''mảng 0 chiều'''
arr2= np.array(43)
print(arr2)
'''mảng 1 chiều'''
arr3 = np.array([1, 2, 3, 4, 5])

print(arr3)
'''mảng 2 chiều'''

arr4 = np.array([[1, 2, 3], [4, 5, 6]])

print(arr4)
'''mảng 3 chiều'''
arr5 = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(arr5)
'''kiểm tra số chiều'''
a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)
arr6= np.array([1, 2, 3, 4], ndmin=5)

print(arr6)
print('number of dimensions :', arr6.ndim)