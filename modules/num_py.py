#import numpy module
import numpy

#creating an array
arr = numpy.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])
print("array =",arr)

#use np keyword instead of numpy
import numpy as np
print("version =",np.__version__) #version of numpy

#creating an array using np keyword
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10,])
print("array =",arr)

#type of an array
print("Type of arr :",type(arr))

# #0D array
arr1 = np.array(42)
print("0D array: ",arr1)

# #1D array
arr2 = np.array([1, 2, 3, 4, 5])
print("1D array: ",arr2)

# #2D array
arr3 = np.array([[1, 2, 3], [4, 5, 6]])
print("2D array: ",arr3)

# #3D array
arr4 = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print("3D array: ",arr4)

#checking Dimesion of array
print(arr1.ndim)
print(arr2.ndim)
print(arr3.ndim)
print(arr4.ndim)

#higher dimension of array
arr5 = np.array([1, 2, 3, 4], ndmin=5)
print(arr5)
print('number of dimensions :', arr5.ndim)

#array indexing
arr6 = np.array([1, 2, 3, 4])
print(arr6[0])

#adds to array
print(arr[2] + arr[3])

#access 2D array
print('2nd element on 1st row: ', arr3[0, 1])
