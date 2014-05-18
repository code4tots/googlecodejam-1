# Based on O(N) solution presented in contest analysis
def solve(N,d,l,D):
	v = sorted(range(N), key = lambda x : d[x])
	
	s = [None] * N
	s[0] = d[0]
	
	i = 0
	j = 1
	
	while max(i,j) < N:
		if s[v[i]] is not None:
			while j < N and s[v[i]] >= d[v[j]] - d[v[i]]:
				s[v[j]] = min(d[v[j]] - d[v[i]], l[v[j]])
				j += 1
		i += 1
	
	for i in range(N):
		if s[v[i]] is not None and s[v[i]] + d[v[i]] >= D:
			return True

for t in range(1,int(input())+1):
	N = int(input())
	d, l = zip(*[map(int,input().split()) for _ in range(N)])
	D = int(input())
	
	print('Case #%d: %s' % (t, ('YES' if solve(N,d,l,D) else 'NO')))
