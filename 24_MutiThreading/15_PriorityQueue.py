""""

q=queue.PriorityQueue()
q.put(priority,element)

"""

import queue
q=queue.PriorityQueue()
q.put((1,'AAA'))
q.put((4,'BBB'))
q.put((3,'CCC'))
q.put((2,'DDD'))

print(q)
while not q.empty():
	print(q.get()[1],end=' ')


