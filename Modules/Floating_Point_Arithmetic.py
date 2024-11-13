# # # Experiments with Floating Point Arithmetic

# import math

# # We expect the following to be false
# print("0.1 + 0.1 + 0.1 == 0.3 is", 0.1 + 0.1 + 0.1 == 0.3)

# # We expect the following to be false
# print("round(0.1, 1) + round(0.1, 1) + round(0.1, 1) == round(0.3, 1) is", round(0.1, 1) + round(0.1, 1) + round(0.1, 1) == round(0.3, 1))

# # We expect the following to be true
# print("math.isclose(0.1 + 0.1 + 0.1, 0.3) is", math.isclose(0.1 + 0.1 + 0.1, 0.3))

# # We expect the following to be true
# print("round((0.1 + 0.1 + 0.1), 1) == round(0.3, 1) is", round((0.1 + 0.1 + 0.1), 1) == round(0.3, 1))

# # We get what we expect

# # # Experiments with Representation

# from decimal import Decimal

# # We expect the following to be true
# print(0.333333333333333314829616256247390992939472198486328125 == 1/3)

# # We expect the following to be true
# print(0.333333333333333314829616256247390992939472198486328125 == Decimal.from_float(1/3))

# # We get what we expect! 