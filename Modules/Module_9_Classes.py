# # # Reminder of Function Syntax

# # We expect the following function to take two positional only arguments, one 
# # positional or keyword arguemnt, collect the remaining positional arguments, 
# # then have one kwarg, and then collect the remaining kwargs
# def luridkiller(arg1, arg2, /, manman, *man, savage = "brodie", **lusinger):
#     print(arg1, arg2, manman, man, savage, lusinger)

# luridkiller("bruh", "tool", "drool", "killer", "whose", savage = "truth", krilla = "manman")

# # We get what we expect! 

# # # Experiments with Classes

# # The following is a dummy class that has two attributes, a piece of data and a 
# # function
# class FooBar: 
#     "a dummy class"
#     truth = True

#     def __init__(self, data, string):
#         self.data = data
#         self.string = string

#     def f(self):
#         return(truth)

# # The following should instantiate an object of the type of our class
# x = FooBar([1,2,3], "polar")

# # The following should print the instantiated attributes of our instance, and 
# # the variable set by the class
# print(x.data, x.string, x.truth)

# # We get what we expect!

# # # Experiments with Functions in Instances

# # The following should define three functions of the class C
# def f1(self, x, y):
#     return min(x, x+y)

# class C:
#     f = f1

#     def g(self):
#         return 'hello world'

#     h = g

# x = C()

# # We expect the following to give us three methods
# print(type(x.f), type(x.g), type(x.h))

# # We get what we expect!

