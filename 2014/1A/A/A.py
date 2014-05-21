def solve(N,L,outs,ins):
	best = L+1
	stack = [(outs,ins,0,0)]
	while stack:
		outs, ins, d, s = stack.pop()

		if set(o[:d] for o in outs) == set(i[:d] for i in ins):
			if d == L:
				if s < best:
					best = s
			else:
				stack.append(
					(
						[tuple(x if j != d else 1-x for j,x in enumerate(o)) for o in outs],
						ins,
						d+1,
						s+1
					)
				)
				stack.append((outs,ins,d+1,s))

	return 'NOT POSSIBLE' if best == L+1 else best

for t in range(1,int(input())+1):
	N, L = map(int,input().split())
	outs = [tuple(map(int,o)) for o in input().split()]
	ins  = [tuple(map(int,i)) for i in input().split()]
	print('Case #%d: %s' % (t,solve(N,L,outs,ins)))
