def solve():
	N, X = map(int,input().split())
	S = sorted(map(int,input().split()))
	
	def test(M):
		A = S[:M]
		B = S[M:]
		U = [False] * M
		
		for b in B:
			for i in reversed(range(M)):
				if not U[i] and A[i] + b <= X:
					U[i] = True
					break
		
		return N - sum(U)
	
	return min(test(m) for m in range(N+1))

for i in range(1,1+int(input())):
	print('Case #%d: %d' % (i,solve()))

