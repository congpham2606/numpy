import numpy as np
arr=np.array([1,2,3,4,5])
print(arr.dtype)
arr1=np.array(['apple', 'banana', 'cherry'])
print(arr1.dtype)
'''tạo mảng với kiểu dữ liệu xác định'''
arr2=np.array([1,2,3,4],dtype='S')
print(arr2)
'''tạo mảng bản sao với kiểu dữ liệu khác'''
arr3 = np.array([1.1, 2.1, 3.1])
newarr=arr.astype('i')
print(newarr)
print(newarr.dtype)