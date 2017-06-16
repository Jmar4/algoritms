arr = [7, 1, 3, 4, 2, 5, 8, 15, 12, 11, 14, 9, 13, 6, 10]

def bubble_sort(arr):
	for x in range(0, len(arr)):
		for k in range(0,len(arr)-1):
			if arr[k] > arr[k+1]:
				tmp = arr[k]
				arr[k] = arr[k+1]
				arr[k+1] = tmp

def printl(arr):
	print("Sorted array:")
	for x in range(0, len(arr)):
		print("%d" %arr[x])

bubble_sort(arr)
printl(arr)