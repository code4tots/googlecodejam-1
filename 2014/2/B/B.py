def solve():
	N = int(input())
	A = list(map(int,input().split()))
	I = max((i for i in range(N)),key=lambda i: A[i])
	
	def test(M):
		B = list(A)
		