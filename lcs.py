'''
	A Python script to read two strings from a file and find their longest common subsequence.
	Also, print the size of the longest common subsequence.
'''

A = 'bacdca'
B = 'adbcda'

n = len(A)
m = len(B)

opt = [[0 for i in range(0,n+2)] for j in range(0,m+2)]
par = [[0 for i in range(0,n+2)] for j in range(0,m+2)]

for i in range(1,n+1):
	for j in range(1,m+1):
		if A[i-1] == B[j-1]:
			opt[i][j] = opt[i-1][j-1] + 1
		elif opt[i][j-1] >= opt[i-1][j]:
			opt[i][j] = opt[i][j-1]
		else:
			opt[i][j] = opt[i-1][j]

print opt[n][m]