import numpy as np
arr=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
newarr=arr.reshape(4,3)
print(newarr)
print(arr.reshape(2,3,2))
arr2 = np.array([1, 2, 3, 4, 5, 6, 7, 8])
a=arr2.copy().base
print(arr2.reshape(2, 4).base)
print(a)
'''reshape tự tính toán'''

arr3 = np.array([1, 2, 3, 4, 5, 6, 7, 8])

newarr3= arr3.reshape(2, 2, -1)

print(newarr3)
'''chuyển mảng đa chiều thành 1 chiều'''
arr4 = np.array([[1, 2, 3], [4, 5, 6]])

newarr4= arr4.reshape(-1)

print(newarr4)
