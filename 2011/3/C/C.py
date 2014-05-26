# Based on official analysis
def solve():
	from networkx import Graph, number_connected_components
	from heap.heap import heap
	
	def up(p):
		r, c = divmod(p,C)
		return (R-1 if r==0 else r-1)*C + c
	
	def down(p):
		r, c = divmod(p,C)
		return (0 if r==R-1 else r+1)*C + c
	
	def left(p):
		r, c = divmod(p,C)
		return r*C + (C-1 if c==0 else c-1)
	
	def right(p):
		r, c = divmod(p,C)
		return r*C + (0 if c==C-1 else c+1)
	
	def link(a,b):
		G.add_edge(('start',a),('end',b))
		H[b] += 1
	
	R, C = map(int,input().split())
	N = R*C
	G = Graph()
	H = heap({n:0 for n in range(N)})
	
	for p in range(N):
		G.add_node(('start',p))
		G.add_node(('end',p))
	
	for p, x in enumerate(x for _ in range(R) for x in input().strip()):
		if x == '|':
			link(p,up(p))
			link(p,down(p))
		elif x == '-':
			link(p,left(p))
			link(p,right(p))
		elif x == '/':
			link(p,down(left(p)))
			link(p,up(right(p)))
		elif x == '\\':
			link(p,up(left(p)))
			link(p,down(right(p)))
	
	while H[H.peek()] <= 1:
		p, ins = H.popitem()
		
		if ins == 0:
			# There is a sqaure such that no other square points to it.
			# It's impossible for a lemming to get here.
			# So there are no proper ways to arrange this.
			return 0
		
		else:
			# There is exactly one edge leading into p.
			# Remove the relevant nodes.
			_, q = next(iter(G['end',p]))
			r = next(r for _, r in G['start',q] if r != p)
			
			G.remove_node(('end',p))
			G.remove_node(('start',q))
			
			# If q now points to p, the other square that q points to
			# has one fewer square pointing to it.
			H[r] -= 1
	
	# Now all remaining nodes are cycles, and there are exatly two ways
	# to choose the directions for each cycle.
	return pow(2,number_connected_components(G),1000003)

for t in range(1,1+int(input())):
	print('Case #%d: %s' % (t,solve()))
