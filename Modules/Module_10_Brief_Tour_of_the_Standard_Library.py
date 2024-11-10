# # # Experiments with String Pattern Matching

# import re

# # The following could should search for words starting with f that end with any 
# # sequence of characters
# match_f = re.findall(r'\bf[a-z]*', 'Throwing Friday fun into four patterned suits')

# print(match_f)

# # The following could should replace pairs of duplicate words with the first 
# # element in the pair
# remove_dupe = re.sub(r'(\b[a-z]+) \1', r'\1', 'Trees on the the porch eating while others play knock knock jokes')

# print(remove_dupe)

# # We see we get what we expect!

# # # Experiments with math, random and statistics modules

# import math
# import statistics
# import random

# def circle_area(radius):
#     """ This function should calculate the area of a circle given its radius 
#     """

#     area = math.pi*(radius**2)

#     return area

# # The following should generate a 100 value list of randomly sampled integers 
# # from 1 to 100, and then should pass this list to the area function defined 
# # above to get the area of circle with radius equal to the randomyl sampled 
# # integers, and then it should take the mean of these values  
# avg_area = statistics.mean(circle_area(x) for x in random.sample(range(1,101),100))

# print(avg_area)

# # We get what we expect!

# # # Experiments with doctest

# import doctest

# def average(values):
#     """ Computes the mean of a list of numbers

#     >>> print(average([23,591,5891]))
#     2168.3333333333335
#     """

#     return (sum(values)/len(values))
    
# # The following should test the function, and then return no errors
# doctest.testmod()

# # We get what we expect

