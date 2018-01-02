N = int(input().strip())
arr = [int(x) for x in input().strip().split()]
def get_next_permutation():
	for i in rangeipiv(N-1,0,-1):
		if(arr[i] > arr[i-1]):
			pivot = i
	for j in range(pivot,N):
		#get j which compliant to j>=i and A[j]>A[i-1]
		if(arr[j] > arr[pivot]):
			pivot2 = j
	arr[pivot], arr[pivot2] = arr[pivot2], arr[pivot]
	for k in range(pivot+1,int((pivot+N)/2)):
		arr[k], arr[N-1-k] = arr[N-1-k], arr[k]
	print(' '.join(arr))

get_next_permutation()
