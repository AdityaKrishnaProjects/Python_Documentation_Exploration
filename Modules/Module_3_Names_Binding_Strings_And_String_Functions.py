# # # Experiments with names and binding

# # We expect this to cause a to be 1, and b to be 3, as the first line binds the object 1 to a,
# # and then we bind the object named by a to b, and then we bind 3 to b.
# a = 1
# b = a
# b = 3

# print("b = ", b)
# print("a = ", a)

# # We expect this to cause both lists to be identical: [2,2,3]
# first_List = [1,2,3]
# second_List = first_List
# second_List[0] = 2

# print("second list =", second_List)
# print("first list =", first_List)

# # We expect this to cause two different lists
# third_List = [1,2,3]
# fourth_List = third_List
# fourth_List = [3,2,1]

# print("fourth list =", fourth_List)
# print("third list =", third_List)

# # We get what we expect!

# # # Messing around with string splicing, and strings

# test_String = "blobalob"

# # This string is 8 characters long, so the list should have entries indexed from 0 to 7
# # We then can think about splicing the string as having the left of the first 'b' be index 0
# # and the right of the last 'b' be index 8. The heuristic for splicing is that the final 
# # piece of the index is always omitted, whereas the first element of the index is always included
# # So even though the list's final index is 7, for splicing we will use 8 as the final index to get 
# # the end of the string. 

# # We expect this to be the string "alob" because it starts at index 4, which is right after the fourth character
# print(test_String[4:8])

# # We expect this to be the string blob, as it ends at index 4, which is character 5

# print(test_String[:4])

# # We then have splicing tools, we can end the splice or start the splice with an empty character to get
# # the end or the start of the string. We can also use negative indices of the string

# # This should produce the same result as above
# print(test_String[4:])

# # As should this
# print(test_String[-4:])

# # And this should produce the string
# print(test_String[:4] + test_String[4:])

# # This worked the way we expected it to.

# # # Experiments with Lists, list splicing and len()

# # We expect the following to empty the middle 3 entries of this 9 entry list for a copy (so both numbers and our new list should be intact)

# numbers = [1,2,3,4,5,6,7,8,9]

# numbers_Copy = numbers[3:6]
# print(numbers_Copy)
# print(numbers)

# # Whereas we expect the following to affect the original object bound by numbers

# numbers_New = numbers
# numbers_New.append(0)
# print(numbers_New)
# print(numbers)

# # We expect the following to give us the number of values in the list (10)

# print(len(numbers))

# # We get what we expect! 

# # # Experiments with nested lists

# # We expect this to give us 5
# numbers_Nested = [[1,2,3],[4,5,6],[7,8,9]]

# print(numbers_Nested[1][1])

# # We get what we expect!

