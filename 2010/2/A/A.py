def solve(k,s,d):
	def test(r,c):
		for dc in range(s):
			try:
				if d[r][c+dc] is not None and d[r][c-dc] is not None and d[r][c+dc] != d[r][c-dc]:
					return False
			except IndexError:
				break
		return True
	
	def find():
		for c in range(s):
			for r in range(s):
				if not test(r,c):
					break
			else:
				yield c
	
	bc = min(find(), key=lambda x : abs(k-1-x))
	d = list(zip(*d))
	br = min(find(), key=lambda x : abs(k-1-x))
	
	bc = abs(k-1-bc)
	br = abs(k-1-br)
	
	return (k+bc+br) ** 2 - k ** 2

for t in range(1,int(input())+1):
	k = int(input())
	s = 2 * k - 1
	d = []
	for _ in range(s):
		d.append([])
		for x in map(int,input().split()):
			d[-1].append(x)
			d[-1].append(None)
		d[-1].pop()
		n = (s-len(d[-1]))//2
		d[-1] = [None] * n + d[-1] + [None] * n
	print('Case #%d: %d' % (t,solve(k,s,d)))

