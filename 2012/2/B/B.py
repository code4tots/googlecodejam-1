# Randomizd solution suggested in analysis
def solve(N,W,L,R):
	from random import uniform
	
	pts = []
	
	def dist2(x,y,xo,yo):
		return abs(x-xo) ** 2 + abs(y-yo) ** 2
	
	def is_good(x,y,r):
		for _, xo, yo, ro in pts:
			if (r+ro) ** 2 >= dist2(x,y,xo,yo):
				return False
		return True
	
	for i in sorted(range(N), key = lambda i : R[i], reverse = True):
		r = R[i]
		while True:
			x = uniform(0.1,W-0.1)
			y = uniform(0.1,L-0.1)
			if is_good(x,y,r):
				break
		pts.append((i,x,y,r))
	
	for _, x, y, _ in sorted(pts):
		yield x
		yield y

for t in range(1,int(input())+1):
	N, W, L = map(int,input().split())
	R = list(map(int,input().split()))
	print('Case #%d: %s' % (t, ' '.join(map(repr,solve(N,W,L,R)))))
