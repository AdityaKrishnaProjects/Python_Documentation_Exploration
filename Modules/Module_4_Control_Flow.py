# # Messing around with string splicing, and strings

# test_String = "blobalob"

# # This string is 8 characters long, so the list should have entried indexed from 0 to 7
# # We then can think about splcing the string as having the left of the first 'b' be index 0
# # and the right of the last 'b' be index 8. The heuristic for splicing is that the final 
# # piece of the index is always omitted, whereas the first element of the heursitic is always included
# # So even though the list's final index is 7, for splicing we will use 8 as the final index to get 
# # the end of the string. 

# # We expect this to be the string "alob" because it starts at index 4, which is right after the fourth character
# print(test_String[4:8])

# # We expect this to be the string blob, as it ends at index 4, which is character 5

# print(test_String[:4])

# # We then have splicing tools, we can end the splice or start the splice with an empty character to get
# # the end or the start of the string. We can also use negative entries of the string

# # This should produce the same result as above
# print(test_String[4:])

# # As should this
# print(test_String[-4:])

# # And this should produce the string
# print(test_String[:4] + test_String[4:])

# Experiments with names and binding

# # Seeing how for loops over strings works

# test_String = "string"

# for letter in test_String:
#    print(letter, len(letter))

# # Iterates over each character as an element of a string, also worth knowing that strings are immutable, so no use iterating over them to try to change letters
# # you would instead use a copy of the string, or construct a new string in the for loop (probably using string concatenation)

# The following shows how we would use for loops over a collection, without modifying the collection in the for loop (which can cause problems)

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


