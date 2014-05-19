def solve(X,S,R,T,OW):
	OW.sort()
	W = []
	last = 0
	for b, e, w in OW:
		if last != e:
			W.append((0,b-last))
		W.append((w,e-b))
		last = e
		
	if last != X:
		W.append((0,X-last))
	
	ans = 0
	for i in sorted(range(len(W)), key = lambda i : W[i]):
		w, l = W[i]
		
		if T == 0:
			ans += l/(S+w)
		
		else:
			if l/(R+w) <= T:
				ans += l/(R+w)
				T -= l/(R+w)
			
			else:
				ans += T
				ans += (l-(R+w)*T)/(S+w)
				T = 0
		
	return ans

for t in range(1,int(input())+1):
	X, S, R, T, N = map(int,input().split())
	OW = [tuple(map(int,input().split())) for _ in range(N)]
	print('Case #%d: %s' % (t,solve(X,S,R,T,OW)))
