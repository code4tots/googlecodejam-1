def memoize(f):
	memo = {}
	def memoized_function(*args):
		if args not in memo:
			memo[args] = f(*args)
		return memo[args]
	return memoized_function

def solve(P,M,price_of):
	inf = float('inf')
	
	def left_of(x):
		return 2 * x + 1
	
	def right_of(x):
		return 2 * x + 2
	
	@memoize
	def rec(match,miss):
		if match >= len(price_of):
			# If we don't have a price for this match, 'match' is not
			# actually a match, but a team. Just make sure we haven't
			# missed more than we are allowed to for this team.
			return 0 if miss <= M[match - len(price_of)] else inf
		
		else:
			# We are considering a real match here.
			# We need to consider the costs of the lesser matches.
			return min(
				rec(left_of(match),miss  ) + rec(right_of(match),miss  ) + price_of[match],
				rec(left_of(match),miss+1) + rec(right_of(match),miss+1))
	
	return rec(0,0)

for t in range(1,int(input())+1):
	P = int(input())
	M = tuple(map(int,input().split()))
	price_of = []
	for _ in range(P):
		price_of.extend(reversed(tuple(map(int,input().split()))))
	price_of.reverse()
	
	print('Case #%d: %d' % (t,solve(P,M,price_of)))
