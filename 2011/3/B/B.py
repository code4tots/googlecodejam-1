def solve():
	N, *nn = map(int,input().split())

	if N == 0:
		# N == 0 is a special case
		return 0

	n = [0] * 10000
	for i in nn:
		n[i-1] += 1
	del nn

	ch   = [float('inf')]
	ans  = float('inf')
	last = None

	for i, c in enumerate(n):
		if c:
			if i-1 == last:
				if c < len(ch):
					ans = min(ans,min(ch[c:]))
					ch  = ch[:c]

				elif c > len(ch):
					ch = [0]*(c-len(ch)) + ch

				ch = [c+1 for c in ch]

			else:
				ans = min(ans,min(ch))
				ch  = [1]*c

			last = i
	ans = min(ans,min(ch))
	return ans

for t in range(1,1+int(input())):
	print('Case #%d: %s'%(t,solve()))
