N = 37

def expected_profit(X,bet):
	m = min(X[i]+bet[i] for i in range(N))
	I = [i for i in range(N) if X[i]+bet[i]==m]
	return 36*sum(bet[i] for i in I)/len(I)-sum(bet)

def fill(X,D,L):
	'''Make bets so that the first D entries are filled up to at least L
	and the remaining N-D entries are filled to at least L+1'''
	bet = [0] * N
	for i in range(D):
		if X[i] < L:
			bet[i] = L - X[i]
	for i in range(D,N):
		if X[i] < L+1:
			bet[i] = L+1 - X[i]
	return bet

def solve(X,B):
	profit = 0
	for D in range(1,37):
		lL = 0
		uL = sum(X) + B
		while lL+1 < uL:
			L = (lL+uL)//2
			bet = fill(X,D,L)
			if sum(bet) > B:
				uL = L
			else:
				lL = L
		bet = fill(X,D,lL)
		profit = max(profit,expected_profit(X,bet))
	return profit

for t in range(1,int(input())+1):
	B, _ = map(int,input().split())
	X = list(map(int,input().split()))
	X += [0] * (N - len(X))
	X.sort()
	print('Case #%d: %s' % (t,solve(X,B)))

