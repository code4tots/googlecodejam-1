def solve():
	from networkx import Graph, max_flow
	W, H, B = map(int,input().split())
	R = [[True for _ in range(H)] for _ in range(W)]
	
	for _ in range(B):
		x0, y0, x1, y1 = map(int,input().split())
		for x in range(x0,x1+1):
			for y in range(y0,y1+1):
				R[x][y] = False
	
	G = Graph()
	
	for x in range(W):
		for y in range(H):
			if R[x][y]:
				G.add_edge(('start',x,y),('end',x,y),capacity=1)
			
				if y == 0:
					G.add_edge('source',('start',x,y))
				else:
					if R[x][y-1]:
						#G.add_edge(('end',x,y),('start',x,y-1))
						pass
				
				if y == H-1:
					G.add_edge(('end',x,y),'sink')
				else:
					if R[x][y+1]:
						G.add_edge(('end',x,y),('start',x,y+1))
	
	return max_flow(G,'source','sink','capacity')

for t in range(1,1+int(input())):
	print('Case #%d: %d' % (t,solve()))
