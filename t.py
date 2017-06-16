def module(x, y):
	if (y-x)<=0:
		r = (y-x)*(-1)
		return(r)
	else:
		return(y-x)

def module2(x, y):
	return(int(x-y))

def half(arr):
	return(int(len(arr)/2)+1)

arr2 = [1, 2, 3, 4, 5]

print("%d" %half(arr2))
print("%d" %module(80, 40))
print("%d" %module2(4, 40))
