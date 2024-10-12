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

# # # Experiments with List Comprehensions

# # The following are equivalent

# # Should produce a list of pairs of elements from both lists that are not equal
# list = [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]

# print(list)

# # Should do the same thing
# combs = []

# for x in [1,2,3]:
#     for y in [3,1,4]:
#         if x != y:
#             combs.append((x, y))

# print(combs)

# # We get the result we expect!

# # # More experiments with list comprehensions

# # Our new list
# vec = [-4, -2, 0, 2, 4]
# # create a new list with the values doubled
# [x*2 for x in vec]
# print(vec)

# # filter the list to exclude negative numbers
# [x for x in vec if x >= 0]
# print(vec)

# # apply a function to all the elements
# [abs(x) for x in vec]
# print(vec)

# # call a method on each element
# freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
# stripped = [weapon.strip() for weapon in freshfruit]
# print(stripped)

# # create a list of 2-tuples like (number, square)
# truth = [(x, x**2) for x in range(6)]
# print(truth)

# # flatten a list using a listcomp with two 'for'
# vec = [[1,2,3], [4,5,6], [7,8,9]]
# vec = [num for elem in vec for num in elem]
# print(vec)

# # We get what we expect! 

