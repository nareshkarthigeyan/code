import random as rn
import copy as cp
i = 0
arr = [1, 5, 6, 3, 2, 4]
cparr = cp.copy(arr)
print("Bogo sort of the array: ", arr)

while True:
	i += 1
	rn.shuffle(cparr)
	arr.sort()
	if(cparr == arr):
		break

print(i, "iterations.")
print("Final array:", cparr)
