import numpy as np
arr=np.array([1,2,3,4])
print(arr[0])
print(arr[1])
print(arr[2] + arr[3])
'''truy cập mảng 2 chiều'''
arr2 = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print('5th element on 2nd row: ', arr2[1,4])
'''truy cập mảng 3 chiều'''
arr3 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr3[0,1,2])
print(arr3[0,1,-1])