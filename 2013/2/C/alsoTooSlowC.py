
def solve(N,A,B):
	from itertools import count
	before = {n:set() for n in range(N)}
	after = {n:set() for n in range(N)}
	
	def link(i,j):
		after[i].add(j)
		before[j].add(i)
	
	last = {}
	for i in range(N):
		if A[i] > 1:
			link(last[A[i]-1],i)
		last[A[i]] = i
	for i in reversed(range(N)):
		if B[i] > 1:
			link(last[B[i]-1],i)
		last[B[i]] = i
	
	
	for i in range(N):
		for j in range(i+1,N):
			if A[i] >= A[j]:
				link(j,i)
			if B[i] <= B[j]:
				link(i,j)
	for i in range(N):
		for j in reversed(range(i)):
			if A[j] == A[i]:
				link(i,j)
				break
		for j in reversed(range(i)):
			if B[j] == B[i]:
				link(j,i)
				break
	'''
	for j in range(N):
		for i in reversed(range(j)):
			if A[i] >= A[j]:
				link(j,i)
				break
		for i in reversed(range(j)):
			if B[i] <= B[j]:
				link(i,j)
				break
	'''	
	
	before = {i:sorted(before[i],reverse=1) for i in range(N)}
	
	less_than = {i:set() for i in range(N) if not before[i]}
	
	for i in range(N):
		stack = [i]
		while stack:
			i = stack.pop()
			if i not in less_than:
				if all(j in less_than for j in before[i]):
					less_than[i] = set(before[i])
					for j in before[i]:
						less_than[i] |= less_than[j]
				else:
					stack.append(i)
					stack.extend(j for j in before[i] if j not in less_than)
	
	answer = [ None ] * N
	stack = sorted(range(N), reverse=1)
	used = set()
	
	while stack:
		i = stack.pop()
		
		if answer[i] is None:
			x = 1
			while x in used:
				x += 1
			
			for j in less_than[i]:
				if answer[j] is None:
					x += 1
					while x in used:
						x += 1
			
			answer[i] = x
			used.add(x)
			stack.extend(j for j in before[i] if answer[j] is None)
			
	return answer
		
	

for t in range(1,int(input())+1):
	N = int(input())
	A = list(map(int,input().split()))
	B = list(map(int,input().split()))
	print('Case #%d: %s' % (t,' '.join(map(str,solve(N,A,B)))))
