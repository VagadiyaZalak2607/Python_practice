#import numpy module
import numpy  

#creating an array
arr = numpy.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])
print("array =",arr)

#use np keyword instead of numpy
import numpy as np
print("version =",np.__version__) #version of numpy

#creating an array using np keyword
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
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
arr3 = np.array([[1, 2, 3,4,5,6,7,8,9,10], [11,12,13,14,15,16,17,18,19,20]]) #row0 and row1
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
print("number of dimensions :", arr5.ndim)

#array indexing
arr6 = np.array([22,23,24,25,26,27,28,29,30])
print("array 1st element: ",arr6[0])
print("array 3rd element: ",arr6[2])

#adds to array
print("3 & 4 element addition: ",arr6[2] + arr6[3])

#access 2D array
print("element between 0 and 1 index number: ", arr3[0, 1])

#slicing
print("array slicing: ",arr[2:10])
print("elements : ",arr[3:]) 
print("elements : ",arr[:4])

#negative slicing
print("elements : ",arr[-3:-1]) 
 
#slicing 2D array
print(arr3[1, 1:4]) #(row,column)
print(arr3[0:2, 2])
print(arr3[0:2, 1:4])

#step
print("step: ",arr[1:5:2])
print("every other element: ", arr[::2]) #every other element from the entire array

#data type
print("data type of array values: ", arr.dtype) 
arr = np.array([1, 0, 3,4,5,0,-1])
newarr = arr.astype(bool) #returns 0 as false
print(newarr)
print(newarr.dtype)

#copy an array
arr = np.array([1, 2, 3, 4, 5])
x = arr.copy() #copy an array
arr[0] = 42 #change 0 index value
print(arr)
print(x)

#changes in view array
arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
x[0] = 31
print(arr)
print(x)