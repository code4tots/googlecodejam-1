def solve(S):
	freqs = []
	letts = []
	
	def parse(s):
		# count the frequencies and letter makeup of each string
		f = []
		l = []
		lc = None
		for c in s:
			if c != lc:
				lc = c
				l.append(c)
				f.append(0)
			f[-1] += 1
		freqs.append(f)
		letts.append(l)
	
	# parse every string
	for s in S:
		parse(s)
	
	# verify that every string has the same letter makeup
	if not all(l == letts[0] for l in letts):
		return 'Fegla Won'
	
	# I thought just setting the target as the average
	# as the right thing to do, but it looks like I seem to get it wrong...
	ans = 0
	freqs = zip(*freqs)
	for fs in freqs:
		best = 10000000
		for target in range(1,101):
			candidate = 0
			for f in fs:
				candidate += abs(f - target)
			
			best = min(best, candidate)
		ans += best
	
	return ans

for t in range(1,int(input())+1):
	N = int(input())
	print('Case #%d: %s' % (t,solve([input().strip() for _ in range(N)])))