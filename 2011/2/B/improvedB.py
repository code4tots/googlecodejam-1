# Same code but most things in function so lookup can be faster.
# also uses arrays instead of hashtables when possible.
# Still takes ~4.5 minutes...
'''
Kyumins-iMac:B kyuminkim$ time bash -c "cat B-large-practice.in | python3 improvedB.py > B-large-practice.out4"

real	4m34.380s
user	4m33.505s
sys	0m0.280s
Kyumins-iMac:B kyuminkim$ 
'''
# Old version takes ~7.5 minutes
'''
real	7m36.603s
user	7m34.797s
sys	0m0.704s
Kyumins-iMac:B kyuminkim$ 
'''

def solve(t):
	def dp2(t):
		'2D dynamic programming'
		d = [[0 for _ in range(C)] for _ in range(R)]
		for r in range(R):
			for c in range(C):
				d[r][c] = t[r][c]
				if r > 0:
					d[r][c] += d[r-1][c]
				if c > 0:
					d[r][c] += d[r][c-1]
				if r > 0 and c > 0:
					d[r][c] -= d[r-1][c-1]
		return d

	def rdp(d,t,r,c,s):
		'Reverse dynamic programming -- extract partial sums (cuts corners)'
		r2 = r + s - 1
		c2 = c + s - 1
		v = d[r2][c2]
		if r > 0:
			v -= d[r-1][c2]
		if c > 0:
			v -= d[r2][c-1]
		if r > 0 and c > 0:
			v += d[r-1][c-1]
		v -= t[r][c] + t[r][c2] + t[r2][c] + t[r2][c2]
		return v

	def cummulative_weight(r,c,s):
		return rdp(CW,W,r,c,s)

	def cummulative_row_weight(r,c,s):
		return rdp(CWR,WR,r,c,s)

	def cummulative_column_weight(r,c,s):
		return rdp(CWC,WC,r,c,s)

	def check(r,c,s):
		'Check if the blade cut from r->r+s-1, and c->c+s-1 has good density'
		cr = r + (r + s - 1)
		cc = c + (c + s - 1)
		w = cummulative_weight(r,c,s)
		return cr * w == 2 * cummulative_row_weight   (r,c,s) and \
			   cc * w == 2 * cummulative_column_weight(r,c,s)
	
	R, C, D = map(int,input().split())
	W   = [[w         for c,w in enumerate(map(int,input().strip()))] for r in range(R)]
	WR  = [[W[r][c]*r for c in range(C)] for r in range(R)]
	WC  = [[W[r][c]*c for c in range(C)] for r in range(R)]
	
	CW  = dp2(W)
	CWR = dp2(WR)
	CWC = dp2(WC)
	
	answer = 1
	for r in range(R-2):
		for c in range(C-2):
			for s in reversed(range(3,min(R-r,C-c)+1)):
				if check(r,c,s):
					answer = max(answer,s)
					break
	
	if answer < 3:
		answer = 'IMPOSSIBLE'
	
	print('Case #%d: %s' % (t,answer))


for t in range(1,int(input())+1):
	solve(t)
