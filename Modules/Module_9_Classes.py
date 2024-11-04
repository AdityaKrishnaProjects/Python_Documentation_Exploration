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

# # # Experiments with dataclasses

# from dataclasses import dataclass

# # Should create a class that bundles pieces of data
# @dataclass
# class Employee:
#     name: str
#     dept: str
#     salary: int

# # Should create an instance of this class and then call its attributes
# blorb = Employee("blorb", "glorbology", 5000000000)

# print(blorb.dept, blorb.salary)

# # We get what we expect

# # # Experiments with next()

# # Should establish a container that can be iterated over
# s = 'abc'

# # Should establish it as an iterator object
# it = iter(s)

# print(it)

# # Should print the returns objects from the next() function
# print(next(it))

# print(next(it))

# print(next(it))

# # Should return the StopIteration exception
# print(next(it))

# # We get what we expect! 

# # # Experiments with implementing __iter__() in classes

# # Should create a class than has its own iterator behavior
# class Reverse:
#     """Iterator for looping over a sequence backwards."""
#     def __init__(self, data):
#         self.data = data
#         self.index = len(data)

#     # Establishes iter behavior, but since we define __next__() we only need to 
#     # return self
#     def __iter__(self):
#         return self

#     # Establishes next behavior. As self.index starts at len() we start by 
#     # decreasing the index by one (so that when the index is called it will 
#     # return the last value of the container), and then we return the value at 
#     # that index. When our index is 0 we raise the StopIteration exception 
#     # (as that means we have already returned the value indexed at 0)
#     def __next__(self):
#         if self.index == 0:
#             raise StopIteration
#         self.index = self.index - 1
#         return self.data[self.index]

# # We expect the following to create a sequence object with the iterator defined 
# # to iterate inversely, and then we expect the for loop to print this reversed 
# # order
# r = Reverse("truth")

# for char in r:
#     print(char)

# # We get what we expect!

# # # Experiments with Generators

# # We expect the following to create a generator function. This function will 
# # return values according to its yield statement which allows for easy creation 
# # of complex iteration procedures
# def reverse(data):
#     # This for loop starts at the final index of our sequence type, and ends 
#     # at -1 (meaning that it will evaluate at index 0), with a step of -1
#     for index in range(len(data)-1, -1, -1):
#         yield data[index]

# # We expect this loop to print the list in reverse
# for n in reverse([1,3,3,5,1,23,5]):
#     print(n)

# # We get what we expect

# # Experiments with Generator Expressions

# We expect the following to return the sum of the odd numbers in the list
print(sum(i for i in range(0, 100, 7) if i % 2 == 1))

# We get what we expect!