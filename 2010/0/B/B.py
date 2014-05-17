from fractions import gcd
from functools import reduce

for t in range(1,int(input())+1):
	num = iter(map(int,input().split()))
	N = next(num)
	num = list(num)
	
	T = -1
	y = None
	
	for n in num:
		g = reduce(gcd,(abs(m-n) for m in num))
		if g > T:
			T = g
			y = 0 if n%g == 0 else ((n//g)+1)*g - n
		elif g == T:
			y = min(y,(0 if n%g == 0 else ((n//g)+1)*g - n))
	
	print('Case #%d: %d' % (t,y))
	