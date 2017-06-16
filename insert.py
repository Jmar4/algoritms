arr = [5, 7, 1, 3, 4]

def insert_sort(arr):
	N = len(arr)
	for k in xrange(1, N):
		for x in xrange(0, k-1):
			if(arr[k-x]<arr[k]):
				tmp = arr[k]
				arr[k] = arr[k-x]
				arr[k-x] = tmp

insert_sort(arr)
print ("Sorted array is:")
for i in range(len(arr)):
    print ("%d" %arr[i])
