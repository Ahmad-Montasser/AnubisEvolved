def tri_recursion(k):
	k=int(k)
	if(k > 0):
		result = k + tri_recursion(k - 1)
		print(result)
	else:
		result = 0
