'''
	A Python script to read two strings from a file and find their longest common subsequence.
	Also, print the size of the longest common subsequence.
	Using the following values for parent array: 
		- 2 for up
		- 1 for left
		- 0 for diagnal
'''

input_file = "input.txt"
output_file = "output.txt"
file_in = open(input_file,"r")
lines = file_in.readlines()
file_in.close()
file_out = open(output_file, "w")

A = lines[0].strip()
B = lines[1].strip()

n = len(A)
m = len(B)

opt = [[0 for i in range(0,m+1)] for j in range(0,n+1)]
par = [[0 for i in range(0,m+1)] for j in range(0,n+1)]

for i in range(1,n+1):
	for j in range(1,m+1):
		if A[i-1] == B[j-1]:
			opt[i][j] = opt[i-1][j-1] + 1
			par[i][j] = 0
		elif opt[i][j-1] >= opt[i-1][j]:
			opt[i][j] = opt[i][j-1]
			par[i][j] = 1
		else:
			opt[i][j] = opt[i-1][j]
			par[i][j] = 2

file_out.write(str(opt[n][m]))

i = n
j = m
S = ''

while i>0 and j>0:
	if par[i][j] == 0:
		S = A[i-1] + S
		i-=1
		j-=1
	elif par[i][j] == 2:
		i-=1
	else:
		j-=1
file_out.write("\n" + S)