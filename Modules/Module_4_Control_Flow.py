# # # Experiments with if statements

# # We expect the following to return 0 if the value is negative or zero, however
# # in the negative case it will modify the value to be equal to 0. It will
# # print single if the value is 1 and more otherwise. We see elif is used to not
# # waste space with indentation. 
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

# # Iterates over each character as an element of a string, also worth knowing 
# # that strings are immutable, so no use iterating over them to try to change 
# # letters you would instead use a copy of the string, or construct a new string
# # in the for loop (probably using string concatenation)

# # # The following shows how we would use for loops over a collection, without 
# # modifying the collection in the for loop (which can cause problems)

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

# # We see that both methods work, I think I prefer creating a new collection, 
# # rather than iterating over a copy. Keeps more of the original data intact 
# # that way

# # # Experiments with range() 

# # We expect the following to generate a list with elements from 2 to 8 but not 
# # include any odd values. 
# print(list(range(2,9,2)))

# # We expect the following to generate a list with elements from -100 to -10 
# # incrementing by -10
# print(list(range(-10, -101,-10)))

# # We get what we expect! 

# # # Experiments with break, continue and else in for or while loops

# # We expect the following range function to start with 2 and give consecutive 
# # integers till 9, so our outermost for loop should conclude after 7 loops
# # inside our for loop the integer is passed to another for loop which runs with 
# # a range from (2,n). We expect the first integer to terminate the loop
# # immediately and trigger the else clause, whereas the next numbers will break 
# # out of the for loop so long as there is a number from 2 to n that cleanly 
# # divides n without integer (% = 0). We will then return n = x * n//x which 
# # should give x multiplied by n/x 
# # (we use floor division but we shouldn't need to)
# for n in range(2, 10):
#     for x in range(2, n):
#         if n % x == 0:
#             print(n, 'equals', x, '*', n//x)
#             break
#     else:
#         # loop fell through without finding a factor
#         print(n, 'is a prime number')

# # We get what we expect!

# # The following is the same code but without floor division, we expect the 
# # same result. 
# for n in range(2, 10):
#     for x in range(2, n):
#         if n % x == 0:
#             print(n, 'equals', x, '*', n/x)
#             break
#     else:
#         # loop fell through without finding a factor
#         print(n, 'is a prime number')

# # We get what we expect, however floats are returned instead of integers as we 
# # used normal division! 

# # The following two code snippets will show why continue is useful in place of 
# # better control flow, break or else

# # The following should tell us the first prime numbers n is divisible by
# for n in range(1, 11):
#     if n % 2 == 0:
#         print("2 is the first prime number that divides", n)
#         continue
#     if n % 3 == 0:
#         print("3 is the first prime number that divides", n)
#         continue
#     if n % 5 == 0: 
#         print("5 is the first prime number that divides", n)
#         continue
#     else:
#         print(n, "is prime")

# # The following should tell us the first prime numbers n is divisible by
# for n in range(11):
#     if n % 2 == 0:
#         print("2 is the first prime number that divides", n)
#     else:
#         if n % 3 == 0:
#             print("3 is the first prime number that divides", n)
#         else:
#             if n % 5 == 0: 
#                 print("5 is the first prime number that divides", n)
#             else:
#                 print(n, "is prime")

# # Both programs execute the same algorithm, but one is far simpler to read

# # # Experiments with match

# # We expect the following to ask for a string, and then return Wrong unless 
# # the string inputted is "the exact word I was thinking of"
# x = input("Give me a string now \n")

# match x:
#     case "the exact word I was thinking of":
#         print("You guessed the exact word I was thinking of")
#     case _:
#         print("Wrong")

# # We get what we expect! 

# # # Experiments with Defining Functions

# # We expect the following to print a list of fibonacci numbers up to n
# def fib(n):
#     """Print a Fibonacci series up to n"""
#     a, b = 0,1
#     while a < n:
#         print(a, end=" ")
#         a, b = b, a+b
#     print()

# fib(2000)

# # We expect the following functions to return a random integer from the 
# # requested indices in a list object
# import random

# def list_Containing_One_Random_Integer(lower_Bound, upper_Bound):
#     """This function returns a random integer from the requested indices 
#     in a list object"""
#     dummy_List = []

#     dummy_List.append(random.randrange(lower_Bound,upper_Bound+1))

#     return dummy_List

# def list_Containing_One_Random_Integer_No_List_Methods(lower_Bound, upper_Bound):
#     """This function returns a random integer from the requested indices in a 
#     list object, but it doesn't use the append method"""
#     dummy_List = []

#     dummy_List = dummy_List + [random.randrange(lower_Bound,upper_Bound+1)]

#     return dummy_List

# # We expect the following code to give us two lists with 100 random integers 
# # from 1 to 10
# dummy_List = []

# for i in range(100):
#     dummy_List.append(list_Containing_One_Random_Integer(1,10))

# print(dummy_List, "\n", "\n")
# print(len(dummy_List), "\n", "\n")

# dummy_List_No_List_Methods = []

# for i in range(100):
#     dummy_List_No_List_Methods.append(list_Containing_One_Random_Integer_No_List_Methods(1,10))

# print(dummy_List_No_List_Methods, "\n", "\n")
# print(len(dummy_List_No_List_Methods), "\n", "\n")

# # We get what we expect! 

# # # Experiments with function parameters

# # We expect the following to be callable without giving arguments
# import random

# def list_Containing_One_Random_Integer(lower_Bound=1, upper_Bound=10):
#     """This function returns a random integer from the requested indices in a 
#     list object, with it's default values being 1-10"""
#     dummy_List = []

#     dummy_List.append(random.randrange(lower_Bound,upper_Bound+1))

#     return dummy_List

# print(list_Containing_One_Random_Integer())

# # We get what we expect

# # We expect the following code snippet to print 0
# i = 0

# def bad_Function(input=i):
#     """This function prints the input, and takes i as the default value"""
#     print(input)

# i = 2

# bad_Function()

# # We get what we expect!

# # We expect the following code snippet to print successive lists, and the 
# # lists to persist between calls of the function
# def f(a, L=[]):
#     L.append(a)
#     return L

# print(f(1))
# print(f(2))
# print(f(3))

# # We get what we expect! 

# # We expect the following to print three successive lists, each containing 
# # the elements of the last
# def f(a, L=[]):
#     L.append(a)
#     return L

# print(f(1))
# print(f(2))
# print(f(3))

# # We get what we expect!

# # We expect the following to print three successive lists, each containing 
# # only one element
# def f(a, L=None):
#     if L is None:
#         L = []
#     L.append(a)
#     return L

# print(f(1))
# print(f(2))
# print(f(3))

# # We get what expect! 

# # # Experiments with Kwargs

# # The following function should accept an arbitrary number of arguments and 
# # kwargs, after having accepted it's stipulated arguments
# def client_Requests(items_Needed, *misc_Requests, **client_Details):
#     """This function should accept the items a client needs, their arbitrary 
#     requests, and their details. It should then print their details, and 
#     if the order can be handled, return the order details"""
    
#     if items_Needed > 10:
#         print("Order rejected! Too many items!")
#         return

#     if client_Details == {}:
#         print("No client details!")
#     else:
#         print("Client details: ")
#         for dt in client_Details:
#             print(dt, ":", client_Details[dt])
    
#     print("-" * 40)

#     print("This order contains", items_Needed, "items")
#     print("This order contains the following requests:")
#     for req in misc_Requests:
#         print(req)

# client_Requests(10, "quick", name="Gorbachev", wealth_status="Truly very wealthy")

# client_Requests(100, name="Greedy Goblin")

# # Works the way we expect! 

# # # Lambda expressions

# # We expect the following code snippet to define a function that accepts 
# # a lambda expression as an argument.  
# def sort_Tuples_Check_For_Duplicates(*, key_value=lambda x: x[0], tuples):
#     """This function accepts a key value (a function) which will
#     determine what the key for our list sort will be. It also accepts the tuples
#     that will be sorted, and then the sorted index of the tuples will be compared
#     to see if there are any duplicate values. The default key value will be 
#     a function that sorts by the first value in the tuple."""
    
#     # Sort the list using the provided key function
#     tuples.sort(key=key_value)

#     # Compare adjacent elements to find duplicates
#     for i in range(len(tuples) - 1):
#         # Compare the elements based on the key value
#         if key_value(tuples[i]) == key_value(tuples[i + 1]):
#             return "duplicate found"
    
#     return "no duplicate found"

# # Test Cases
# apples = [('b', 'e'), ('g', 'h'), ('a', 'a'), ('f', 'd'), ('c', 'g')]
# oranges = [('b', 'e'), ('b', 'h'), ('a', 'a'), ('f', 'd'), ('c', 'g')]
# multi_tuples = [('x', 'y', 1), ('a', 'b', 2), ('x', 'z', 1), ('c', 'd', 3)]


# print(sort_Tuples_Check_For_Duplicates(tuples=apples))  
# print(sort_Tuples_Check_For_Duplicates(tuples=apples, key_value=lambda tuple: tuple[1]))  
# print(sort_Tuples_Check_For_Duplicates(tuples=oranges))
# print(sort_Tuples_Check_For_Duplicates(tuples=multi_tuples, key_value=lambda x: x[1]))
# print(sort_Tuples_Check_For_Duplicates(tuples=multi_tuples))

# # We get what we expect! 

