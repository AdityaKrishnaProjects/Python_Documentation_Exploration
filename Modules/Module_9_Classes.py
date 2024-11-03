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

# # # Experiments with name mangling

# # We expect the following to create a class that has one instance variable, this 
# # variable is assigned to by the update method defined in the class when an 
# # instance is created. This class has one function (update), that appends items 
# # in the iterable given to the class to the unassignable instance variable.  
# class Mapping:
#     def __init__(self, iterable):
#         self.items_list = []
#         self.__update(iterable)

#     def update(self, iterable):
#         for item in iterable:
#             self.items_list.append(item)

#     __update = update   # private copy of original update() method

#     # Should still work even after subclass redefines update
#     def update_twice(self, iterable):
#         self.__update(iterable)
#         self.__update(iterable)

# # This is a derived class of the Mapping class that has a different update 
# # method. This new method takes two arguments, keys and values, zips them and 
# # then appends them to the instance variable. Even though MappingSubClass 
# # redefines update, it doesn't break __init__(), as when init calls __update 
# # it refers to its private copy of the original update() method
# class MappingSubclass(Mapping):

#     def update(self, keys, values):
#         # provides new signature for update()
#         # but does not break __init__()
#         for item in zip(keys, values):
#             self.items_list.append(item)

# class MappingSubClassThatChangesNothing(Mapping):
#     pass

# # The following should create an instance of the Mapping object and then update 
# # its items_list, and then print its items list
# x = Mapping([0])

# x.update([1,2,3])

# print(x.items_list)

# # The following should create an instance of the MappingSubClass object and 
# # then update its items_list, and then print its items list
# y = MappingSubclass([(0,0)])

# y.update([1,2,3], [3,2,1])

# print(y.items_list)

# # The following should call the update_twice() function on a MappingSubClass 
# # instance which will refer to the original update function
# y.update_twice([1,2,3])

# print(y.items_list)

# # The following should use the original update function
# i = MappingSubClassThatChangesNothing([0])

# i.update([3,2,1])

# print(i.items_list)

# # We get what we expect! 

