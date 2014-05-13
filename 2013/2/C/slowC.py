def solve(N,A,B):
	r = [ None ] * N # list to fill in with the ordering
	rr = dict() # inverse mapping of r
	bs = dict()
	stack = [ (1,0,1,1) ]
	while stack:
		# 'x' is next number to put into 'r'
		# 'i' is next position to try to insert x into
		# 'a' is the value A[i] where 'x' is to be inserted
		# 'b' is the value B[i] where 'x' is to be inserted
		x, i, a, b = stack.pop()
		
		if x in rr:
			# if we have 'x' inserted into 'r' from a previous
			# try, we need to wipe it
			r[rr[x]] = None
			del rr[x]
		
		for i in range(i,N):
			if r[i] is None:
				if A[i] == a and B[i] == b:
					# Valid candidate!
					r[i] = x
					rr[x] = i
					
					if x == N:
						# If we have put in all numbers 1 .. N,
						# we have found a solution!
						return r
					
					else:
						# We still need to put in numbers x+1 .. N.
						
						# In case we fail with current configuration,
						# we add entry in stack so we can try next position
						stack.append( (x,i+1,a,b) )
						
						# Now we add entry in stack to find a place for 'x+1'
						# However, finding the b's when going from left to right
						# is not trivial. So we precalculate the b's.
						bs[x+1] = [1]
						for j in reversed(range(N)):
							if r[j] is not None:
								bs[x+1].append(max(bs[x+1][-1],B[j]+1))
						stack.append( (x+1,0,1,bs[x+1].pop()) )
						
						# No need to continue this loop since we found place
						# for 'x'.
						break
			else:
				# We encounter an entry that could change 'a' and 'b'
				a = max(a,A[i]+1)
				b = bs[x].pop()

for t in range(1,int(input())+1):
	N = int(input())
	A = list(map(int,input().split()))
	B = list(map(int,input().split()))
	print('Case #%d: %s' % (t, ' '.join(map(str,solve(N,A,B)))))
