# # # Experiments with if statements

# # We expect the following to return 0 if the value is negative or zero, however in the negative case it will modify the value to be equal to 0. It will
# # print single if the value is 1 and more otherwise. We see elif is used to not waste space with indentation. 
# x = int(input("Please enter an integer: "))

# if x < 0:
#     x = 0
#     print('Negative changed to zero')
# elif x == 0:
#     print('Zero')
# elif x == 1:
#     print('Single')
# else:
#     print('More')

# # We get what we expect! 

# # We will now try to do the same thing but not using elif
# x = int(input("Give a number: "))

# if x < 0:
#     x = 0 
#     print('Negative changed to zero')
# else:
#     if x == 0:
#         print("Zero")
#     else: 
#         if x == 1:
#             print("Single")
#         else: 
#             print("More")

# # We see that the body is huge, but we still get what we expect. 

# # # Experiments with for loops over strings works

# test_String = "string"

# for letter in test_String:
#    print(letter, len(letter))

# # Iterates over each character as an element of a string, also worth knowing that strings are immutable, so no use iterating over them to try to change letters
# # you would instead use a copy of the string, or construct a new string in the for loop (probably using string concatenation)

# # # The following shows how we would use for loops over a collection, without modifying the collection in the for loop (which can cause problems)

# # Create a sample collection
# users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}

# # Strategy:  Iterate over a copy
# for user, status in users.copy().items():
#     if status == 'inactive':
#         del users[user]
# print(users)

# # Strategy:  Create a new collection
# active_users = {}
# for user, status in users.items():
#     if status == 'active':
#         active_users[user] = status
# print(active_users)

# # We see that both methods work, I think I prefer creating a new collection, rather than iterating over a copy. Keeps more of the original data intact that way

# # # Experiments with range() 

# # We expect the following to generate a list with elements from 2 to 8 but not include any odd values. 
# print(list(range(2,9,2)))

# # We expect the following to generate a list with elements from -100 to -10 incrementing by -10
# print(list(range(-10, -101,-10)))

# # We get what we expect! 

# # Experiments with break

