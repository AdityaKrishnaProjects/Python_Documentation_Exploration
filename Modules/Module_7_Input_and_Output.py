# # # Experiments with f-string usage

# bird = "parrot"

# status = "dead"

# # The following code should print using an fstring
# print(f'my bird is a {bird} and it\'s status is {status}')

# # We get what we expect!

# # # Experiments with f-string parameters

# # The following should print consistently lined up columns of data
# table = {'Sjoerd': 4127, 'Jack': 4098999, 'Dcab': 7678}
# for name, phone in table.items():
#     print(f'{name:10} ==> {phone:10d}')

# # We get what we expect! 

# # Experiments with str.format()

# # Experiments with referencing dictionary keys in an f-string

# # The following should print the value associated with
# # the key in the dictionary
# table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
# print('Jack: {0[Jack]}; Sjoerd: {0[Sjoerd]}; '
#       'Dcab: {0[Dcab]}'.format(table))

# # We get what we expect

# # Experiments with reducing dictionary to kwargs

# # We expect the following to print the values for their associated keys
# table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
# print('Jack: {Jack}; Sjoerd: {Sjoerd}; Dcab: {Dcab}'.format(**table))

# # We get what we expect! 

# # # Experiments with str.center()

# commands = "you will do what I say"

# # We expect the following to print 10 centered strings, with total line length 
# # being 70 characters
# for x in range(10):
#     print(commands.center(70+x))

# # We get what we expect! 

# # # Experiments with jsons

# import json

# # We expect the following to print the json
# x = [1, 'simple', 'list']
# print(json.dumps(x))

# # We get what we expect