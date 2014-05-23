# WATCH OUT FOR FLOATING POINT!!
# My original solution involved calculating key as L[i]/1-P[i]/100.
# Works for small input, but generates wrong answer for large input!!
class Key:
	def __init__(self,ilp):
		i, lp = ilp
		l, p = map(int,lp)
		self.i = i
		self.l = l
		self.p = 100 - p
	
	def __lt__(self,other):
		return 100 * self.l + self.p * other.l < 100 * other.l + other.p * self.l
	
	def __repr__(self):
		return str(self.i)

for t in range(1,int(input())+1):
	int(input())
	print('Case #%d: %s' % (t,' '.join(map(str,sorted(map(Key,enumerate(zip(input().split(),input().split()))))))))
