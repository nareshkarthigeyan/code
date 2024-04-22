import random as rn
import copy as cp
import math as mt

i = 0
arr = [1, 5, 6, 3, 2, 4, 9]
cparr = cp.copy(arr)
print("Bogo sort of the array: ", arr)

iterations = []

for j in range(10):
	while True:
		i += 1
		rn.shuffle(cparr)
		arr.sort()
		if(cparr == arr):
			break
	iterations.append(i)

	print(i, "iterations.")

print("Final array:", cparr)
prob = 1 / mt.factorial(len(arr))
print("The probablity of each iteration is happening is: ", prob)
print("Number of iterations in 10 tries are:", iterations)
