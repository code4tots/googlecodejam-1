def solve(N,M,zip_of,flights):
	def still_possible():
		# still_possible() asks if there is still some way to visit all
		# the cities given the current configuration
		hypothetically_visited = set(visited) # set of cities we can hypothetically visit.
		
		def recurse(city):
			# dfs to try to hypothetically visit all cities starting from city.
			hypothetically_visited.add(city)
			for neighboring_city in neighbors_of[city]:
				if neighboring_city not in hypothetically_visited:
					recurse(neighboring_city)
		
		current_hypothetical_city = current_city
		
		while current_hypothetical_city is not None:
			recurse(current_hypothetical_city)
			current_hypothetical_city = parent_of[current_hypothetical_city]
		
		return len(hypothetically_visited) == N
	
	starting_city = min(range(1,N+1), key = lambda city : zip_of[city]) # city where you start
	current_city = starting_city # current location
	parent_of = {starting_city:None} # parent_of[c] is the city that we came from when we visit c for the first time.
	neighbors_of = {city:set() for city in range(1,N+1)}
	for a, b in flights:
		neighbors_of[a].add(b)
		neighbors_of[b].add(a)
	visited = {starting_city} # set of all visited cities
	answer = [zip_of[starting_city]] # list of zipcodes so far collected.
	
	while len(visited) < N:
		visitable = set()
		current_hypothetical_city = current_city
		while current_hypothetical_city is not None:
			for neighboring_city in neighbors_of[current_hypothetical_city]:
				if neighboring_city not in visited:
					visitable.add(neighboring_city)
			current_hypothetical_city = parent_of[current_hypothetical_city]
		
		# We want to go to the city with the smallest zipcode we can.
		# However, we also must make sure that all cities are still visitable.
		last_city = current_city
		while True:
			next_city = min(visitable, key = lambda city : zip_of[city])
			
			current_city = last_city
			while next_city not in neighbors_of[current_city]:
				current_city = parent_of[current_city]
			
			parent_of[next_city] = current_city
			visited.add(next_city)
			current_city = next_city
			
			if still_possible():
				break
			
			del parent_of[next_city]
			visited.remove(next_city)
			visitable.remove(next_city)
		
		answer.append(zip_of[current_city]) # We just visited this city for the first time! add to zipcode.
		visited.add(current_city) # Mark as visited
	
	return ''.join(map(str,answer))

for t in range(1,int(input())+1):
	N, M = map(int,input().split())
	zip_of = [None] + [int(input()) for _ in range(N)]
	flights = [list(map(int,input().split())) for _ in range(M)]
	print('Case #%d: %s' % (t,solve(N,M,zip_of,flights)))

	
	