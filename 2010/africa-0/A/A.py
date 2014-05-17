for t in range(1,int(input())+1):
	C = int(input())
	I = int(input())
	P = list(map(int,input().split()))
	a, b = 0, 0
	for i, ip in enumerate(P):
		for j, jp in enumerate(P):
			if i == j:
				continue
			
			if ip + jp == C:
				a, b = i, j
				break
		else:
			continue
		break
	
	print('Case #%d: %d %d' % (t,a+1,b+1))

