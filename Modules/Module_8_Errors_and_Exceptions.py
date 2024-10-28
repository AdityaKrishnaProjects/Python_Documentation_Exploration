# # # Experiments with derived classes and exceptions

# # Should raise B, C and D in that order
# class B(Exception):
#     pass

# class C(B):
#     pass

# class D(C):
#     pass

# for cls in [B, C, D]:
#     try:
#         raise cls()
#     except D:
#         print("D")
#     except C:
#         print("C")
#     except B:
#         print("B")

# # Should raise B, B, and B
# for cls in [B, C, D]:
#     try:
#         raise cls()
#     except B:
#         print("B")
#     except C:
#         print("C")
#     except D:
#         print("D")

# # We get what we expect! 

# # # Experiments with exception arguments

# # Should print the type of inst (exception class), the arguments of the 
# # exception after it is raised, the arguments should be printed again as 
# # __str__() is defined to print all arguments without accessings .args, and 
# # then it should unpack the arguments
# try:
#     raise Exception('spam', 'eggs')
# except Exception as inst:
#     print(type(inst))    # the exception type
#     print(inst.args)     # arguments stored in .args
#     print(inst)          # __str__ allows args to be printed directly,
#                          # but may be overridden in exception subclasses
#     x, y = inst.args     # unpack args
#     print('x =', x)
#     print('y =', y)

# # We get what we expect! 

# # Experiments with else statements after try statements

# # We expect the following to try to read the file, print the line length, or 
# # print OSError if an OSError occurs while opening the file.
# for arg in sys.argv[1:]:
#     try:
#         f = open(arg, 'r')
#     except OSError:
#         print('cannot open', arg)
#     else:
#         print(arg, 'has', len(f.readlines()), 'lines')
#         f.close()

# # We get what we expect

# # # Experiments with finally statements

# # This code should ask for a number, not end unless you give it the right 
# # number and curse you on the way out
# def vindictivenumberwanter():
#     try:
#         integer = input("Give me a number")
#         while integer != 21081231237807230187:
#             print("wrong number")
#     finally:
#         print("I WILL GET YOU")

# vindictivenumberwanter()

# # We get what we expect!

# # # Experiments with finally and return statements

# # This could should execute the finally statement's return statement
# def bool_return():
#     try:
#         return True
#     finally:
#         return False

# print(bool_return())

# # We get what we expect! 

# # # Experiments with with statements

# # The following code should open the file and close it regardless of if the 
# # file reaches its final line
# with open("myfile.txt") as f:
#     for line in f:
#         print(line, end="")

# # We get what we expect