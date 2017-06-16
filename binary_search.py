def arr_gen(length):
	for k in xrange(0,length-1):
		arr[k] = k+1
	return(arr)

def module(x, y):
	if (y-x)<=0:
		r = (y-x)*(-1)
		return(r)
	else:
		return(y-x)

def half(arr):
	return(int(arr/2)+1)

def bsearch(arr, x):
	prelim1 = 1
	prelim2 = len(arr)
	lim = module(prelim1, prelim2)
	while lim > 0:
		prelim1 = half(len(arr))
		if x < prelim1:
			prelim2 = arr[1]
		elif x > prelim1:
			prelim2 = arr[len(arr)]
		elif x == prelim1:
			break
		lim = module(prelim1, prelim2)
		for x in xrange(prelim1,prelim2):
			arrtmp[x] = arr[x]
		del arr
		for x in xrange(0, len(arrtmp)):
			arr[x] = arrtmp[x]
	print("Search done")


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
bsearch(arr, 2)



