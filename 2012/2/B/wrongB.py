# First attempt.
# Passed the sample, but 
# ran out of room even in the small test case...
class Grid(object):
	def __init__(self,x,y,dx,dy):
		self.x = x
		self.y = y
		self.dx = dx
		self.dy = dy
		self.occupied = False
		self.cx = self.cy = None
		self.children = []
	
	def insert(self,r):
		if self.occupied:
			for child in self.children:
				if child.insert(r):
					return True
			return False
		
		else:
			if self.x == 0:
				x = 0
			elif self.x + self.dx == W:
				x = W
			else:
				if r > self.dx:
					return False
				x = self.x + r
			
			if self.y == 0:
				y = 0
			elif self.y + self.dy == L:
				y = L
			else:
				if r > self.dy:
					return False
				y = self.y + r
			
			if x + r < self.x + self.dx:
				self.children.append(Grid(x+r, y, (self.x+self.dx-x-r)/2, self.dy))
			
			if y + r < self.y + self.dy:
				self.children.append(Grid(x,y+r,self.dx,(self.y+self.dy-y-r)/2))
			
			if x + r < self.x + self.dx and y + r < self.y + self.dy:
				self.children.append(Grid(
					x+r,y+r,
					(self.x+self.dx - x - r)/2,
					(self.y+self.dy - y - r)/2))
			
			self.cx = x
			self.cy = y
			self.occupied = True
			return True
	
	def __iter__(self):
		if self.occupied:
			yield self.cx, self.cy
			for child in self.children:
				for x, y in child:
					yield x, y
	
for t in range(1,int(input())+1):
	N, W, L = map(int,input().split())
	g = Grid(0,0,W,L)
	for r in reversed(sorted(map(int,input().split()))):
		if not g.insert(r):
			raise Exception('could not insert ' + str(r))
	print('Case #%d: %s' % (t,' '.join(str(x) for pair in g for x in pair)))

