import numpy as np
# list =[10,2,30,4,50,6]
# print(type(list))
# np1Array = np.array(list);   # converting list to numpy array 
# print(type(np1Array))
# np2Array = np.array([[1,2,3],[4,5,6]]);
# print(type(np2Array))
# # special arrays 
# zeros = np.zeros((3,3));
# ones = np.ones((4,4))
# print(zeros)
# print(ones)
# rng = np.random.randint(10)
# print(rng)
# # few num array function 
# print(np1Array.ndim)
# print(np2Array.ndim)
# print(np2Array.shape)
# print(ones.shape)
# print(np1Array.size)
# print(np2Array.size)
# print(np1Array.sum())
# print(np2Array.sum())
# print(np1Array.max())
# print(np2Array.min())
# a = np.array([10,20,30,40])
# b = np.array([1,2,3,4])
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)

# num = np.array([10,20,-30,40,50,-90,0,100,-20]);
# print(num)
# print(num[0])       # retrieve element using index position 
# print(num[-1])
# print(num[1:3])
# # boolean index concept 
# positive = num[num>0]
# print(positive)
# negative = num[num<0]
# print(negative)
# # 
# arr = np.arange(12);
# print(arr)
# reshaped = arr.reshape(3,4)
# print(reshaped)

# Broadcasting 

# A = np.array([[1,2,3],[4,5,6]]);
# B= np.array([1,2,3]);
# C = np.array([[1,2,3],[4,5,6]])
# print(A+B)
# print(A+C)

# aggregate function 
# num = np.array([[1,2,3],[4,5,6]])
# print(num.sum())
# print(np.sum(num,axis=1))
# print(np.sum(num,axis=0))
# print(np.mean(num,axis=1))
# print(np.mean(num,axis=0))
# print(np.max(num,axis=1))

# solving linear expression 
# 2x+y=8
# x+3y=13

A = np.array([[2,1],[1,3]])
B = np.array([8,13])
result = np.linalg.solve(A,B)
print(result)