def solve():
	def shoelace(P):
		# Find area of polygon P by using shoelace theorem.
		N = len(P)
		X, Y = zip(*P)
		return abs(sum(X[i]*Y[i+1]-X[i+1]*Y[i] for i in range(-N,0)))/2

	def intersect(p,q,x):
		# return y value of line p<->q at x
		x1, y1 = p
		x2, y2 = q
		return ((y1-y2)/(x1-x2))*(x-x1)+y1

	def cut(x):
		# Assume there are points to left and right of x
		i  = next(i for i,(a,b) in enumerate(L) if a >= x)
		P  = list(L[:i])
		P.append((x,intersect(L[i-1],L[i],x)))
		i  = next(i for i,(a,b) in enumerate(U) if a >= x)
		P.append((x,intersect(U[i-1],U[i],x)))
		P.extend(reversed(U[:i]))
		return shoelace(P)

	def find(t):
		# find x such that cut(x) would be t
		DELTA = 10 ** -6
		a = L[0 ][0]
		b = L[-1][0]
		while a+DELTA < b:
			x = (a+b)/2
			c = cut(x)
			if c > t:
				b = x
			else:
				a = x
		return a

	W, L, U, G = map(int,input().split())
	L = tuple(tuple(map(int,input().split())) for _ in range(L))
	U = tuple(tuple(map(int,input().split())) for _ in range(U))

	t = shoelace(L + tuple(reversed(U))) / G

	return [find(t*i) for i in range(1,G)]


for t in range(1,int(input())+1):
	print('Case #%d:\n%s'%(t,'\n'.join(map(str,solve()))))



