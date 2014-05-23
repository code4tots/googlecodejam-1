# large solution is rather slow, but ok.
def solve(N,G):
	a = N
	for r in range(1,N+1):
		v = { r : None } # v[n] gives parent of n in tree rooted at r
		b = dict() # b[n] gives largest binary subtree starting at n
		stack = [(r,False)]
		while stack:
			n, t = stack.pop()
			if t is False:
				stack.append((n,True))
				for m in (G[n]-{v[n]}):
					v[m] = n
					stack.append((m,False))
			else:
				if len(G[n] - {v[n]}) >= 2:
					b[n] = sum(b[c] for c in sorted(G[n]-{v[n]}, key = lambda m : b[m])[-2:]) + 1
				else:
					b[n] = 1
		a = min(a,N-b[r])
	return a

for t in range(1,int(input())+1):
	N = int(input())
	G = {n:set() for n in range(1,N+1)}
	for _ in range(N-1):
		a, b = map(int,input().split())
		G[a].add(b)
		G[b].add(a)
	print('Case #%d: %d' % (t,solve(N,G)))
