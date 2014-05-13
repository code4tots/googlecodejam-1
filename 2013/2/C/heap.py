class heap(list):
	'''
	wrapper around Python's builtin heapq functions.
	
	C-implementation of heapq is really fast, but I can't update a task's 
	priority with just the heapq functions.
	
	Code is essentially from here:
	https://docs.python.org/3/library/heapq.html#priority-queue-implementation-notes
	
	I use names 'add' and 'pop' instead of 'add_task' and 'pop_task' because
	they are nicer names. However, if heapq fails to load a C implementation,
	there will be weird behavior as the Python implementation relies on list.pop.
	
	I thought I could get around this by passing super(heap,self) instead of self to
	heapq functions, but the C implementation complains if the object you pass to it
	isn't actually a list.
	
	I also modified the code so that by default it uses the task itself as the priority,
	unless a priority is explicitly given. This is a more intuitive behavior for a heap
	than the behvior of the code in the docs, where the heap behaves like a fifo queue if you
	don't explicitly specify priorities.
	
	'''
	
	_REMOVED = object() # sentinel to indicate a removed task
	
	def __init__(self,xs,priorities=None):
		from heapq import heapify
		from itertools import count
		
		xs = list(xs)
		counter = count()
		if priorities is None:
			priorities = list(xs)
		
		super(heap,self).__init__([priority, next(counter), task] for priority, task in zip(priorities,xs))
		self._entry_finder = {entry[-1]:entry for entry in self}
		self._counter = counter
		heapify(self)
	
	def add(self,task,priority=None):
		'Add a new task or update the priority of an existing task'
		from heapq import heappush
		
		if priority is None:
			priority = task
		
		if task in self._entry_finder:
			self.remove(task)
		
		entry = [priority, next(self._counter), task]
		self._entry_finder[task] = entry
		heappush(self,entry)
	
	def remove(self,task):
		'Mark an existing task as REMOVED. Raise KeyError if not found.'
		self._entry_finder.pop(task)[-1] = self._REMOVED
	
	def pop(self):
		'Remove and return the lowest priority task. Raise KeyError if empty.'
		from heapq import heappop
		while self:
			priority, count, task = heappop(self)
			if task is not self._REMOVED:
				del self._entry_finder[task]
				return task
		raise KeyError('pop from an empty priority queue')

