# Python version based on C-version
# C-version is almost instantaneous,
# whereas the Python version is rather slow...
'''
Kyumins-iMac:A kyuminkim$ time bash -c "cat A-large-practice.in | python3 A.py"
Case #1: NO
Case #2: NO
Case #3: NO
Case #4: YES
Case #5: NO
Case #6: YES
Case #7: YES
Case #8: YES
Case #9: YES
Case #10: NO
Case #11: YES
Case #12: YES
Case #13: YES
Case #14: YES
Case #15: YES
Case #16: NO
Case #17: NO
Case #18: NO
Case #19: YES
Case #20: NO
Case #21: YES
Case #22: YES
Case #23: NO
Case #24: YES
Case #25: NO
Case #26: YES
Case #27: NO
Case #28: NO
Case #29: YES
Case #30: YES

real	1m24.474s
user	1m24.418s
sys	0m0.042s

'''
for t in range(1,int(input())+1):
	N = int(input())
	d, l = zip(*[map(int,input().split()) for _ in range(N)])
	D = int(input())
	
	v = sorted(range(N), key = lambda x : d[x])
	
	m = [None] * N
	
	for i in reversed(range(N)):
		a = v[i]
		
		if d[a] >= D:
			break
		
		m[a] = (D-d[a]) if (d[a]+l[a]>=D) else float('inf')
		
		for j in range(i+1,N):
			b = v[j]
			
			if (d[b] > d[a] + l[a]) or (d[b] >= D):
				break
			
			if m[b] <= (d[b]-d[a]):
				m[a] = d[b] - d[a]
				break
	
	print('Case #%d: %s'%(t,('YES' if (m[0] <= d[0]) else 'NO')))

