
def solve(N,A,B):
	neighbor_table = {n:set() for n in range(N)}
	
	def link(i,j):
		neighbor_table[i].add(j)
	
	def neighbors_of(i):
		for j in tuple(neighbor_table[i]):
			if j in neighbor_table:
				yield j
			else:
				neighbor_table[i].discard(j)
	
	last = {}
	for i in range(N):
		if A[i] > 1:
			link(i,last[A[i]-1])
		last[A[i]] = i
	
	for i in reversed(range(N)):
		if B[i] > 1:
			link(i,last[B[i]-1])
		last[B[i]] = i
	
	answer = [None] * N
	used = set()
	def number_of_numbers_less_than_or_equal_to_number_at(i):
		# excludes positions for which numbers are already assigned.
		nums = set([i])
		stack = [i]
		while stack:
			j = stack.pop()
			for k in neighbors_of(j):
				if k not in nums:
					nums.add(k)
					stack.append(k)
		return sum(1 for n in nums if answer[n] is None)
	
	def compute_answer_at(i):
		n = number_of_numbers_less_than_or_equal_to_number_at(i)
		x = 1
		for x in range(1,N+1):
			if x not in used:
				n -= 1
			
			if n == 0:
				used.add(x)
				answer[i] = x
				return
	
	for i in range(N):
		compute_answer_at(i)
	
	return answer
			
		
	

for t in range(1,int(input())+1):
	N = int(input())
	A = list(map(int,input().split()))
	B = list(map(int,input().split()))
	print('Case #%d: %s' % (t, ' '.join(map(str,solve(N,A,B)))))
