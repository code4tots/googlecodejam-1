for t in range(1,int(input())+1):
	A, B = map(int,input().split())
	P = tuple(map(float,input().split()))
	p = P[0]
	d = A - 1
	e = B + 2
	while True:
		e = min(e, d + (B-A+d+1) + (1-p)*(B+1))
		if d == 0:
			break
		p *= P[-d]
		d -= 1
	print('Case #%d: %s' % (t,e))

