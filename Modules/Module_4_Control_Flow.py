# Seeing how for loops over strings works

test_String = "string"

for letter in test_String:
   print(letter, len(letter))

# Iterates over each character as an element of a string, also worth knowing that strings are immutable, so no use iterating over them to try to change letters
# you would instead use a copy of the string, or construct a new string in the for loop (probably using string concatenation)

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


