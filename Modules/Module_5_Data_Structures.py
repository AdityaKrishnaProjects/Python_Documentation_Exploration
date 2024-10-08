# # # Experiments with using lists as queues

# # This code snippet should remove and add items to the front of the list
# from collections import deque
# queue = deque(["Eric", "John", "Michael"])
# queue.append("Terry")           # Terry arrives
# queue.append("Graham")          # Graham arrives

# print(queue) # We expect to see Terry and Graham at the end of the queue

# print(queue.popleft())                 # The first to arrive now leaves

# print(queue.popleft())                 # The second to arrive now leaves

# print(queue)                           # Remaining queue in order of arrival

# queue.appendleft('John')

# print(queue)                           # John is added to start of queue

# # We get what we expect! 

# # Experiments with List Comprehensions

