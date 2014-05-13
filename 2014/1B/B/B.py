'''
Runs way too slow in the worst case (A = 10 ** 9, B = 10 ** 9, K = 1),
but the test cases doesn't test this (even the large one).

Even with the practice large input, the test runs almsot instantaneously.
Code jam's practice judge seems to be happy with the output.
'''
def solve(A,B,K):
	dk = K.bit_length()
	def dfs(a,b,x):
		if a >= A or b >= B or (a&b) >= K:
			return 0
		
		if x == 1:
			return 1 if a&b < K else 0
		
		if (a&b) + x <= K:
			return min(x, B-b) * min(x, A-a)
		
		x >>= 1
		
		return sum(dfs(a+da,b+db,x) for da in (0,x) for db in (0,x))
	
	return dfs(0,0,1 << 30)

for t in range(1,int(input())+1):
	A, B, K = map(int,input().split())
	print('Case #%d: %d' % (t,solve(A,B,K)))
