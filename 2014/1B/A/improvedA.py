'''
Kyumins-iMac:A kyuminkim$ time cat A-large-practice.in | python3 improvedA.py > A-large-practice.out

real	0m0.422s
user	0m0.414s
sys	0m0.008s
Kyumins-iMac:A kyuminkim$ time cat A-large-practice.in | python3 A.py > A-large-practice.out2

real	0m2.208s
user	0m2.200s
sys	0m0.008s
Kyumins-iMac:A kyuminkim$ diff A-large-practice.out{,2}
Kyumins-iMac:A kyuminkim$ 

'''

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
	
	ans = 0
	freqs = zip(*freqs)
	for fs in freqs:
		best = 10000000
		
		ss = [ 0 ] * 101
		cs = [ 0 ] * 101
		fs = sorted(fs)
		j = 0
		for i in range(1,101):
			ss[i] = ss[i-1]
			cs[i] = cs[i-1]
			while j < len(fs) and fs[j] <= i:
				ss[i] += fs[j]
				cs[i] += 1
				j += 1
		total = sum(fs)
		for target in range(1,101):
			candidate = (cs[target] - (len(fs)-cs[target])) * target - ss[target] + (total-ss[target])
			
			best = min(best, candidate)
		ans += best
	
	return ans

for t in range(1,int(input())+1):
	N = int(input())
	print('Case #%d: %s' % (t,solve([input().strip() for _ in range(N)])))