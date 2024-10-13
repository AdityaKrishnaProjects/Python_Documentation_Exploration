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

# # # Experiments with tuples

# # Should produce a three valued tuple
# t = 12345, 54321, 'hello!'
# print(t[0])

# print(t)

# # Tuples may be nested:
# u = t, (1, 2, 3, 4, 5)
# print(u)

# # but they can contain mutable objects:
# v = ([1, 2, 3], [3, 2, 1])
# print(v)

# # Empty tuples are constructed using empty parentheses
# empty = ()
# print(empty)
# print(len(empty))

# # Singleton tuples are constructed using a trailing comma
# singleton = 'hello',
# print(singleton)
# print(len(singleton))

# # We get what we expect

# # # Experiments with Sets

# # The following operations should show basic membership testing and removal of 
# # duplicates
# basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
# print(basket)                      # show that duplicates have been removed

# print('orange' in basket)               # fast membership testing

# print('crabgrass' in basket)

# # Demonstrate set operations on unique letters from two words
# a = set('abracadabra')
# b = set('alacazam')
# print(a)                                  # unique letters in a

# print(a - b)                           # letters in a but not in b

# print(a | b)                              # letters in a or b or both

# print(a & b)                             # letters in both a and b

# print(a ^ b)                              # letters in a or b but not both

# # We get what we expect

# # # Experiments with Dictionaries

# # This should instantiate the dictionary
# tel = {'jack': 4098, 'sape': 4139}
# tel['guido'] = 4127

# print(tel)

# print(tel['jack'])

# # This should delete the element of the dictionary associated with the key 'sape'
# del tel['sape']
# tel['irv'] = 4127
# print(tel)

# # Can use the list statement to transform dictionaries to lists
# print(list(tel))

# # Should return a sorted list of the keys of our dictionary
# print(sorted(tel))

# # Should test for dictionary membership for the keys
# print('guido' in tel)

# print('jack' not in tel)

# # We get what we expect! 

# # # Further experiments with dicts

# # Should construct a dictionary using the dict function
# tel = dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])

# print(tel)

# # Should construct a dictionary using a dict expression
# keys = {x: x**2 for x in (2, 4, 6)}

# print(keys)

# # When the keys are simple strings it is sometimes easier to specify pairs 
# # using keyword arguments
# tel = dict(sape=4139, guido=4127, jack=4098)

# print(tel)

# # We get what we expect

# # # Experiments with Looping Techniques

# # Dictionary looping
# knights = {'gallahad': 'the pure', 'robin': 'the brave'}

# # We expect that this will return a list of two place tuples
# print(knights.items())

# # Should print the successive keys and values in knights
# for k, v in knights.items():
#     print(type(k))
#     print(type(v))
#     print(k, v)

# # Should print the values of our list, with their keys being 0 through 2
# for i, v in enumerate(['tic', 'tac', 'toe']):
#     print(i, v)

# # Should loop over both lists, where the lists are combined into a list of 
# # two place tuples
# questions = ['name', 'quest', 'favorite color']
# answers = ['lancelot', 'the holy grail', 'blue']

# # Zip is an iterator, so we expect it will return a zip type object
# l = zip(questions,answers)

# print(l)

# for q, a in zip(questions, answers):
#     print('What is your {0}?  It is {1}.'.format(q, a))

# # Reversed should reverse the order of a list (so in this case should return 
# # 9 through one, only including odds)
# for i in reversed(range(1, 10, 2)):
#     print(i)

# # Should loop over a sequence in a sorted order, using the sorted() method
# basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
# for i in sorted(basket):
#     print(i)

# # Should print the list in order but without duplicates
# basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
# for f in sorted(set(basket)):
#     print(f)

# # The following should return a list without the NaNs
# import math
# raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
# filtered_data = []
# for value in raw_data:
#     if not math.isnan(value):
#         filtered_data.append(value)

# print(filtered_data)

# # We get what we expect! 

# # # Experiments with conditions

# # We expect the following to assign 'Trondheim' to non_null
# string1, string2, string3 = '', 'Trondheim', 'Hammer Dance'
# non_null = string1 or string2 or string3
# print(non_null)

# # We get what we expect! 

# # # Experiments with comparing sequences and other types

# # We expect the following to be true
# comp1 = ((1, 2, 3) < (1, 2, 4))
# print(comp1)

# # We expect the following to be true
# comp2 = ([1, 2, 3] < [1, 2, 4])
# print(comp2)

# # We expect the following to be true
# comp3 = ('ABC' < 'C' < 'Pascal' < 'Python')
# print(comp3)

# # We expect the following to be true
# comp4 = ((1, 2, 3, 4) < (1, 2, 4))
# print(comp4)

# # We expect the following to be true
# comp5 = ((1, 2) < (1, 2, -1))
# print(comp5)

# # We expect the following to be true
# comp6 = ((1, 2, 3) == (1.0, 2.0, 3.0))
# print(comp6)

# # We expect the following to be true
# comp7 = ((1, 2, ('aa', 'ab')) < (1, 2, ('abc', 'a'), 4))
# print(comp7)

# # We get what we expect