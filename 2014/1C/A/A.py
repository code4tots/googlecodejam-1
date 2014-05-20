from fractions import gcd
for t in range(1,int(input())+1):
	P, Q = map(int,input().split('/'))
	g = gcd(P,Q)
	P //= g
	Q //= g
	if 2 ** 40 % Q == 0:
		P *= 2 ** 40 // Q
		print('Case #%d: %d' % (t,41-P.bit_length()))
	else:
		print('Case #%d: impossible' % (t,))

