# Preface

This file will serve as my general notes on the python documentation. The headings of this markdown file will correspond to the different chapters in the table of contents for Python Documentation as of September 2024, starting on Module 3. Within this note I will reference the modules and experiments I did with them, the code for these modules I experimented with and the results of these experiments will be housed in the modules folder.

## Module 3 - An Informal Introduction to Python

### Basics

In python everything is an object. When we declare a variable, we are really binding a name to an object. From then on this name will be used to refer to this object. 

### Experiments with names and binding

Names and binding is a bit strange, so some experiments with basic data types should make it a bit clearer: 

```
# Experiments with names and binding

# We expect this to cause a to be 1, and b to be 3, as the first line binds the object 1 to a,
# and then we bind the object named by a to b, and then we bind 3 to b.
a = 1
b = a
b = 3

print("b = ", b)
print("a = ", a)

# We expect this to cause both lists to be identical: [2,2,3]
first_List = [1,2,3]
second_List = first_List
second_List[0] = 2

print("second list =", second_List)
print("first list =", first_List)

# We expect this to cause two different lists
third_List = [1,2,3]
fourth_List = third_List
fourth_List = [3,2,1]

print("fourth list =", fourth_List)
print("third list =", third_List)

# We get what we expect!
```

We see the way this works is intuitive! When we declare a variable, we start reading from the right where the object is created, and then we get the object bound to a list. For examples 1 and 3, there is nothing to explain, as new objects are created and then names are bound to them. For example 2, we see that fourth_List is bound to third_List, which is an object we have already declared. Then when we edit fourth_List we are editing the object named by both third_List and fourth_List! 

### Strings 

Strings are stored as lists, and so you can reference their entries as you would in a list. Strings are immutable so you can not edit them like normal lists. 

### Splicing

This works by taking the name binded to the object created and then applying [] with indices to this name. Example: 

```
# Messing around with string splicing, and strings

test_String = "blobalob"

# This string is 8 characters long, so the list should have entries indexed from 0 to 7
# We then can think about splicing the string as having the left of the first 'b' be index 0
# and the right of the last 'b' be index 8. The heuristic for splicing is that the final 
# piece of the index is always omitted, whereas the first element of the index is always included
# So even though the list's final index is 7, for splicing we will use 8 as the final index to get 
# the end of the string. 

# We expect this to be the string "alob" because it starts at index 4, which is right after the fourth character
print(test_String[4:8])

# We expect this to be the string blob, as it ends at index 4, which is character 5

print(test_String[:4])

# We then have splicing tools, we can end the splice or start the splice with an empty character to get
# the end or the start of the string. We can also use negative indices of the string

# This should produce the same result as above
print(test_String[4:])

# As should this
print(test_String[-4:])

# And this should produce the string
print(test_String[:4] + test_String[4:])
```

We see a couple things here, strings are stored as lists of characters as we know, and therefore when we splice with them we respected the indices the list data type gives us (starts at 0 and ends at n-1 of the number of items in the list). We can then think of the string as being split up with 0 being to the left of the first character and n being to the right of the last character when we use splices which always include the first index but exclude the final index. 

We also have negative indices for strings, which start at -n to the left of the first character and end at -1 to the left of the final character. A good heuristic is you will get n values if you input -n as your negative index. 

We also have an empty splice, which to the left gives the first character and to the right gives the last character. 

### Lists

Lists (like all other sequence types) can be indexed and spliced. Lists also suppport concatenation. Lists, unlike strings, are mutable. You can also add new items to the list using list.append(). 

Simple assignment doesn't copy data, so as we have seen above, when you bind a name 'new_Name' to a name 'old_Name' that is already bound to an object, 'new_Name' will simply be bound to the extant list object named by 'old_Name'. To counteract this we can use the slice operation ([:]). 

The following experiments elucidate some behaviors of lists: 

```
# We expect the following to empty the middle 3 entries of this 9 entry list for a copy (so both numbers and our new list should be intact)

numbers = [1,2,3,4,5,6,7,8,9]

numbers_Copy = numbers[3:6]
print(numbers_Copy)
print(numbers)

# Whereas we expect the following to affect the original object bound by numbers

numbers_New = numbers
numbers_New.append(0)
print(numbers_New)
print(numbers)

# We expect the following to give us the number of values in the list (10)

print(len(numbers))

# We get what we expect! 
```

As we can see we the results are what we expect. List assignment binds the new name to the old object, and to get around this we can use splices with empty indices to get a copy of the list. Finally length works as we expect and gives us the number of values in the list (and not the final index which is n-1, where n is the number of values in the list).

A good thing to note is that lists can nest other lists, and the way we access entries is by doubling up on the indices like this: 

```
# We expect this to give us 5
numbers_Nested = [[1,2,3],[4,5,6],[7,8,9]]

print(numbers_Nested[1][1])

# We get what we expect!
```

The first index gives us the value in the outermost list, which we would expect, and then we must specify further if we want a specific element of the list that we just indexed, then we must provide another index for that value (if we don't then it will just return the list at the index given for our outermost list).

### Indentation

This is critically important to the syntax of python. Indentation is python's way of grouping statements. The body of any control flow construct will be indented. 

### Appendix

You can assign multiple variables in one line in python 

```
a, b = 1, 2
```

This will give us a = 1 and b = 2. Python evaluates the right hand side first, and it reads the right hand side from left to right (which is perfect as we can have operations complete on the righthand side before assignment to a name, and these operations will occur in an expected order of operations).

In python any non-zero integer value is true, whereas zero is false. In any sequence anything with a non-zero length is true, whereas empty sequences are false. 

## Module 4 - More Control Flow Tools

### If statements

```
x = int(input("Please enter an integer: "))

if x < 0:
    x = 0
    print('Negative changed to zero')
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else:
    print('More')
```

elif is used in place of doing an else and then an indented if after if statements to avoid excessive indentation statements with further if statments. Trying the same thing without elif: 

```
# We will now try to do the same thing but not using elif

x = int(input("Give a number: "))

if x < 0:
    x = 0 
    print('Negative changed to zero')
else:
    if x == 0:
        print("Zero")
    else: 
        if x == 1:
            print("Single")
        else: 
            print("More")

# We see that the body is huge, but we still get what we expect. 
```

### Indentation for control flow

It is important to realise that indentation gives the control flow construct the instructions for what to do if its condition is met. With this in mind, it makes sense that the else construct is on the same line as the if construct, as if it was inside of the body of if, then else would execute after if executed, whereas we know they represent two different paths for execution of the program. This is why elif is useful, as without if the new if would be in the body of else, and then we would get cascading else constructs for multiple cases. For comparing the same value to several constants or checking for specific types or attributes we might use the match statement. 

### for Statements

### Seeing how for loops over strings works

```
test_String = "string"

for letter in test_String:
   print(letter, len(letter))
```

output: 
```
s 1
t 1
r 1
i 1
n 1
g 1
```

Length of each character was 1 which we would expect, and the loop iterates over each character in the string. 

### Range()

The range() function is useful for creating arithmetic progressions to loop over. These progressions start at 0, and as a result of this fact they match the indices of a list. For example: range(10) generates 10 values, 0 through 9 the legal indices for a sequence of length 10. The specific paramters for the range function include its start, its end and the increment (or the step). It will include the start value as the first value in the progression, and the last value is omitted, as in sequence splicing. Negative indices are also accepted as in splicing. For example: 

```
# # Experiments with range() 

# We expect the following to generate a list with elements from 2 to 8 but not include any odd values. 
print(list(range(2,9,2)))

# We expect the following to generate a list with elements from -100 to -10 incrementing by -10
print(list(range(-10, -101,-10)))

# We get what we expect! 
```

Here we see that the first parameter of range() is the first element of the arithmetic progression, the second parameter is the final value (excluded), and the final parameter is the increment size (or step). 

range() is explicitly handy for interating over the indices of a sequence when combined with len(), as len will give you the number of elements in the sequence n, and then range will give you an arithemtic progression from 0 to n-1, which cleanly is the indices of the sequence. In these cases, people typically use the enumerate() function. 

We notive that when we try to print range, we don't get a list object as we might expect. This is because range() behaves as if it is a list, but it actually is an object which returns the successive items of the desired sequence when you iterate over it, but doesn't really make a list, saving space. These objects are called iterable, suitable as a target for functions and constructs that expect something from which they can obtain successive items until the supply is exhausted. for is an example of such a construct, an example of a function that takes an iterable is sum(). 

### Break and else in for or while loops

The break statement breaks out of the body of the innermost enclosing for or while loop. A for or while loop can also include an else clause. In a for loop else is executed after the loop reaches its final iteration, in a while loop else is executed after the loop's condition becomes false. In either clause the else is not executed if the loop is terminated by a break. 

The following is an illustrative example: 

```
# We expect the following range function to start with 2 and give consecutive integers till 9, so our outermost for loop should conclude after 7 loops
# inside our for loop the integer is passed to another for loop which runs with a range from (2,n). We expect the first integer to terminate the loop
# immediately and trigger the else clause, whereas the next numbers will break out of the for loop so long as there is a number from 2 to n that cleanly 
# divides n without integer (% = 0). We will then return n = x * n//x which should give x multiplied by n/x (we use floor division but we shouldn't need to)
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')

# We get what we expect!

# The following is the same code but without floor division, we expect the same result. 
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n/x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')

# We get what we expect, however floats are returned instead of integers as we used normal division! 
```

We see that break takes us out of for loops, which stops the else condition from triggering, we also see that range when given an index where the start and end are the same returns no value and the for loop immediately terminates, triggering the else condition. In review, a for or while clause's else triggers when no break occurs. 

### Continue

continue is useful because it allows you to stop the current path of execution and restart the loop you are in without using many elses. Example shown below: 

```
# The following should tell us the first prime numbers n is divisible by
for n in range(1, 11):
    if n % 2 == 0:
        print("2 is the first prime number that divides", n)
        continue
    if n % 3 == 0:
        print("3 is the first prime number that divides", n)
        continue
    if n % 5 == 0: 
        print("5 is the first prime number that divides", n)
        continue
    else:
        print(n, "is prime")

# The following should tell us the first prime numbers n is divisible by
for n in range(11):
    if n % 2 == 0:
        print("2 is the first prime number that divides", n)
    else:
        if n % 3 == 0:
            print("3 is the first prime number that divides", n)
        else:
            if n % 5 == 0: 
                print("5 is the first prime number that divides", n)
            else:
                print(n, "is prime")
```

With cascading if statements we would get every prime number that divides n, not only the first prime number that divides n. With cascading statements it is a very messy piece of code. We can't use break as that would break us out of the for loop. 

### pass

The pass statement does nothing. It can be used when a statement is required syntactically but the program requires no action. For example we might have an if where we want an else, but we don't want the else to do anything. 

### match

The match statement is a pattern matching construct that is superficially similar to switch in C, but is more like other pattern matching constructs in other languages. Only the first pattern it matches gets executed and it can also extract components from the value it is passed (sequence elements or object attributes). We can use _ as a wild card variable which will never fail to match. If no case matches none of the branches are executed. 

The following example shows some basic comparison of string literals:

```
# We expect the following to ask for a string, and then return Wrong unless the string inputted is "the exact word I was thinking of"
x = input("Give me a string now \n")

match x:
    case "the exact word I was thinking of":
        print("You guessed the exact word I was thinking of")
    case _:
        print("Wrong")

# We get what we expect! 
```

We see that match works the way we expect. What remains to be seen is how the variables in match are managed, are they both names and variables? Or are they names with no object attached?

We can combine several literals in a single case pattern using the or operator "|". We can bind variables using match statements, as we see in the following example: 

```
# point is an (x, y) tuple
match point:
    case (0, 0):
        print("Origin")
    case (0, y):
        print(f"Y={y}")
    case (x, 0):
        print(f"X={x}")
    case (x, y):
        print(f"X={x}, Y={y}")
    case _:
        raise ValueError("Not a point")
```

Here we have an object point that is passed to match, this object is an x,y tuple, and we have cases that specifically bind the values passed by this object 'point' to names x and y. This answers our question above and tells us match when comparing can bind a passed object or its values to (a) new name(s). When comparing literals, we don't have to declare a name and then bind that name to an object, as our literals are our objects. 

If you are using classes to structure your data (and therefore the expression you are giving to match is a class), then when you are passing the class to match, on each case statement you can simply use the class name followed by an argument list resembling a constructor, but with the ability to capture attributes into variables. This is illustrated by the following example: 

```
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def where_is(point):
    match point:
        case Point(x=0, y=0):
            print("Origin")
        case Point(x=0, y=y):
            print(f"Y={y}")
        case Point(x=x, y=0):
            print(f"X={x}")
        case Point():
            print("Somewhere else")
        case _:
            print("Not a point")
```

In the above example, we see that case accepts Point, the name of our class, and then we have our comparisons occuring over literals in some cases and variables in others. In the case where they are occuring over variables our statemnt of case specifies the pattern we are looking for (e.g. (x=x, y=0)), and then we compare the passed object to this and execute the code in the body of the first case statement that is matched. 

We can add if clauses to the case statements, these are known as "gaurds". The value capture of the comparison occurs before the gaurd is evaluated. When using the or operator "|" we must have our alternatives bind the same variable. This is because we don't want the variable which is to be bound to be unclear. We can use the 'as' expression in case statements to bind whatever pattern is on its left side to the name on the right side. This is useful as if we have a match statement that accepts many different literals for its second value, we want to be able to refer to the value that was matched.

### Defining Functions

The keyword def introduces a function definition. It must be followed by the function name and the parenthesized list of formal parameters. The statements that form the body of the function start at the next line and must be indented. The first statement can be a string literal, this string is the function's documentation string or docstring. The parameters (arguments) to a function call are introduced in the local symbol table of the function when the function is called. Arguments are passed using a call by value, where the value is always an object reference, not the value of the object. When a function calls another function or calls itself recursively, a new local symbol table is created for that call. A function definition associates the function name with the function object in the current symbol table, this means that you can associate a different name with this function object and access the function. 

Functions without return statements return a value called None, a built in name. Writing the value None is normally supressed if it would be the only value written, but if you want to see if you can print the result of a function with no return statement. You can also write return without an expression after it, or fall of the end of a function without a return statement to have a function return None. 

Methods are functions that belong to an object. Methods are function specific, and are called using the obj.methodname syntax. Different types define different methods, and different types may have methods with the same name without causing ambiguity. 

As an example the following uses the method append() for list objects, and uses some function calls: 

```
# We expect the following functions to return a random integer from the requested indices in a list object
import random

def list_Containg_One_Random_Integer(lower_Bound, upper_Bound):
    "This function returns a random integer from the requested indices in a list object"
    dummy_List = []

    dummy_List.append(random.randrange(lower_Bound,upper_Bound+1))

    return dummy_List

def list_Containg_One_Random_Integer_Without_Using_List_Methods(lower_Bound, upper_Bound):
    "This function returns a random integer from the requested indices in a list object, but it doesn't use the append method"
    dummy_List = []

    dummy_List = dummy_List + [random.randrange(lower_Bound,upper_Bound+1)]

    return dummy_List

# We expect the following code to give us two lists with 100 random integers from 1 to 10
dummy_List = []

for i in range(100):
    dummy_List.append(list_Containg_One_Random_Integer(1,10))

print(dummy_List, "\n", "\n")
print(len(dummy_List), "\n", "\n")

dummy_List_Created_Without_Using_List_Methods = []

for i in range(100):
    dummy_List_Created_Without_Using_List_Methods.append(list_Containg_One_Random_Integer_Without_Using_List_Methods(1,10))

print(dummy_List_Created_Without_Using_List_Methods, "\n", "\n")
print(len(dummy_List_Created_Without_Using_List_Methods), "\n", "\n")
```

We get a couple of the results we were looking for: local variables can be named the same thing as other local variables in other functions and no problems arise, similarly when we call our function we notice the append method works the same as appending manually. 

### More on Defining Functions

#### Default values

It is possible to define functions with a variable number of arguments. There are three forms, which can be combined. 

Firstly, you can establish default values which allow the function to be called without those arguments as it will instantiate with default values. 

An edited version of the function written above with default values added is given below: 

```
# We expect the following to be callable without giving arguments
import random

def list_Containing_One_Random_Integer(lower_Bound=1, upper_Bound=10):
    "This function returns a random integer from the requested indices in a list object, with it's default values being 1-10"
    dummy_List = []

    dummy_List.append(random.randrange(lower_Bound,upper_Bound+1))

    return dummy_List

print(list_Containing_One_Random_Integer())
```

This works the way we expect it to. 

The default values are evaluated at the point of function definition in the defining scope of the function. So something like: 

```
# We expect the following code snippet to print 0
i = 0

def bad_Function(input=i):
    "This function prints the input, and takes i as the default value"
    print(input)

i = 2

bad_Function()
```

We see that we get what expect! As the name i was bound to the object 0 when the function was defined in the program, the default value was bound to 0 as well. Even though the function was called after the definition of i was changed, this did not change the default value. 

The default value is evaluated only once. If we have a default value, that is then used and modified within the function, then on successive calls of that function that default value will not be what it was initially, it will be whatever the object's final state was at the end of the last function call. An illustrative example of that is in the following code snippet: 

```
# We expect the following to print three successive lists, each containing the elements of the last. 
def f(a, L=[]):
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))
```

We get what we expect! The default variable L, is changed in the first function call to include the integer 1 as the first value in the list it refers to. This then means in the subsequent function call, we get a list with two values. 

If we don't want the default value to be shared between subsequent function calls, we would need to make the default value equal to None, and then we would have to have a conditional in the function that will set None to the default value we want to share between calls. This is illustrated below in a modified version of the above function: 

```
# We expect the following to print three successive lists, each containing only one element
def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))
```

We get the behaviour we expect! 

#### Keyword Arguments

Keyword arguments are a way in which functions can be called. You specify the name of the argument in the parameters, and then set that argument equal to the value you want to pass to the function. After calling keyword arguments, you can not pass values without specifying the keyword as in positional arguments. You can not provide a duplicate value for the same keyword either. Order is not important for keyword arguments. 

When a final formal parameter of the form **name is present, it receives a dictionary containing all keyword arguments except for those corresponding to a formal parameter. This can be combined with the formal parameter *name which receives a tuple containing all the positional arguments beyond the formal parameter list. *name must occur before **name. This means we can have a function that accepts an arbitrary number of arguments and kwargs, and the arguments beyond the formal parameters that we specify will be stored in a list referred to by the name after the asterisk in *name1 and the kwards will similarly be stored in a dictionary referred to by the name after the asterisk in **name2. 

An example is shown in the following code snippet: 

```
# The following function should accept an arbitrary number of arguments and 
# kwargs, after having accepted it's stipulated arguments
def client_Requests(items_Needed, *misc_Requests, **client_Details):
    """This function should accept the items a client needs, their arbitrary 
    requests, and their details. It should then print their details, and 
    if the order can be handled, return the order details"""
    
    if items_Needed > 10:
        print("Order rejected! Too many items!")
        return

    if client_Details == {}:
        print("No client details!")
    else:
        print("Client details: ")
        for dt in client_Details:
            print(dt, ":", client_Details[dt])
    
    print("-" * 40)

    print("This order contains", items_Needed, "items")
    print("This order contains the following requests:")
    for req in misc_Requests:
        print(req)

client_Requests(10, "quick", name="Gorbachev", wealth_status="Truly very wealthy")

client_Requests(100, name="Greedy Goblin")
```

We see here we get our positional arguments that are unspecified by the function stored in a list named misc_Requests, and we get kwargs that are unspecified by the function stored in a dictionary named client_Details. 

#### Special Parameters

/ and * are special parameters that indicate the kind of parameter and how the arguments may be passed to the function. / means positional only, * means keyword only, and neither means both are acceptable. Arguments linearly preceeding the / argument are positional only, arguments linearly succeeding * are keyword only. Keyword only arguments are also referred to as named parameters. 

The positional only parameters are useful as if you have a double star argument and an unspecified argument, it would typically be impossible to have the double star argument accept a kwarg whose key is the name of the unspecified argument, however using positional only, you can specify the first argument as positional only, and then have the second argument have a key that is the name of the first argument. In other words, the names of positional-only parameters can be used in **kwds without ambiguity.

In general: 

1. Use positional only if you want the name of the parameters to not be available to the user. This is useful when parameter names have no real meaning, if you want to enforce the order of the arguments when function is called, or if you need to take some positional paramters and arbitrary keywords (the case discussed above).
2. Use keyword only when names have meaning and the function definition is more understandable by being explicit with names, or if you want to prevent users relying on the position of the argument being passed. 
3. For an API, use positional-only to prevent breaking API changes if the parameter's name is modified in the future. 

### Arbitrary Argument Lists

Use one star before the name of the argument to specify a variadic argument. This argument will accept all remaining arguments and when referred to by its name it represents a list of all these arguments. Further kwargs can occur after this argument, but any further arguments will not be grammatical. This makes sense, as the * symbol when used as a parameter by itself makes all further arguments kwargs. 

### Unpacking Argument Lists

Using * when specifying arguments in a function call unpacks the elements of the starred named object so the function will accept them as separate positional arguments. Using ** before a named dictionary object in a functiona call works the same way. 

### Lambda Expressions

Small anonymous functions can be created with the lambda keyword. The lambda keyword is the name of the function, the words preceding the colon are the arguments, and the words following the colon is the expression. The expression is limited to one line. The following code snippet uses lambda expressions: 

```
# We expect the following code snippet to define a function that accepts 
# a lambda expression as an argument.  
def sort_Tuples_Check_For_Duplicates(*, key_value=lambda x: x[0], tuples):
    """This function accepts a key value (a function) which will
    determine what the key for our list sort will be. It also accepts the tuples
    that will be sorted, and then the sorted index of the tuples will be compared
    to see if there are any duplicate values. The default key value will be 
    a function that sorts by the first value in the tuple."""
    
    # Sort the list using the provided key function
    tuples.sort(key=key_value)

    # Compare adjacent elements to find duplicates
    for i in range(len(tuples) - 1):
        # Compare the elements based on the key value
        if key_value(tuples[i]) == key_value(tuples[i + 1]):
            return "duplicate found"
    
    return "no duplicate found"

# Test Cases
apples = [('b', 'e'), ('g', 'h'), ('a', 'a'), ('f', 'd'), ('c', 'g')]
oranges = [('b', 'e'), ('b', 'h'), ('a', 'a'), ('f', 'd'), ('c', 'g')]
multi_tuples = [('x', 'y', 1), ('a', 'b', 2), ('x', 'z', 1), ('c', 'd', 3)]


print(sort_Tuples_Check_For_Duplicates(tuples=apples))  
print(sort_Tuples_Check_For_Duplicates(tuples=apples, key_value=lambda tuple: tuple[1]))  
print(sort_Tuples_Check_For_Duplicates(tuples=oranges))
print(sort_Tuples_Check_For_Duplicates(tuples=multi_tuples, key_value=lambda x: x[1]))
print(sort_Tuples_Check_For_Duplicates(tuples=multi_tuples))
```

This example illustrates how lambda expressions work. Here we have a lambda expression that unpacks a tuple to the single element in the tuple we care about. This lambda expression accepts the variable x (which it must be passed when it is called), and then it returns the value at the index of x specified by the lambda expressions right hand side. 

### Docstrings 

The first line should be a short concise summary of the object's purpose. It shouldn't state the object's name or type, as you can access those through other means. Should begin with a capital letter and end with a period. 

The second line should be blank, and then further lines can describe the object's calling conventions, side effects, etc. 

### Function Annotations

Annotations can be made to both the arguments and the return value for the function. For arguments, place a colon after the name of the argument and specify a type, for the return write an arrow like so: -> and then include the type that the function should return. These are completely optional and have no effect on the function. 

### Coding Style

4 spaces for indentation. For functions use names like lowercase_with_underscores, and for classes use names like UpperCamelCase. 

## Module 5 - Data Structures 

### List methods 

Methods are functions associated with a specific class. 

`list.append(x)` adds an item to the end of the list, equivalent to `a[len(a):] = [x]`.

`list.extend(iterable)` extends the list by appending all the items from the iterable. Equivalent to `a[len(a):] = iterable`.

`list.insert(i, x)` inserts an item at a given position. The first argument is the index of the element before which to insert, so `a.insert(0, x)` inserts at the front of the list, and `a.insert(len(a), x)` is equivalent to `a.append(x)`.

`list.remove(x)` removes the first item from the list whose value is equal to x. It raises a ValueError if there is no such item.

`list.pop([i])` removes the item at the given position in the list, and return it. If no index is specified, `a.pop()` removes and returns the last item in the list. It raises an IndexError if the list is empty or the index is outside the list range.

`list.clear()` removes all items from the list. Equivalent to `del a[:]`.

`list.index(x[, start[, end]])` returns zero-based index in the list of the first item whose value is equal to x. Raises a ValueError if there is no such item.

The optional arguments start and end are interpreted as in the slice notation and are used to limit the search to a particular subsequence of the list. The returned index is computed relative to the beginning of the full sequence rather than the start argument.

`list.count(x)` returns the number of times x appears in the list.

`list.sort(*, key=None, reverse=False)` sorts the items of the list in place (the arguments can be used for sort customization, see sorted() for their explanation).

`list.reverse()` reverses the elements of the list in place.

`list.copy()` returns a shallow copy of the list. Equivalent to `a[:]`.

Some data types don't have a defined ordering, and similarly mixed data types often don't have defined orders, so those lists wouldn't be sortable. Methods that just modify the list don't return anything. This is a design decision in python. 

### Using Lists as Stacks

To use lists as stacks where the last item added is the first item retrieved, use `list.append()` and `list.pop()`. 

### Using Lists as Queues

It is also possible to use lists as queues, where the first element added is the first retrieved. Here you would use `list.append()` and `list.pop([0])`, but this is slow as it inserts and pops shifting all other elements over by 1. Instead use `collections.deque`, which was designed to have fast appends and pops from both ends. For example: 

```
# # Experiments with using lists as queues

# This code snippet should remove and add items to the front of the list
from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")           # Terry arrives
queue.append("Graham")          # Graham arrives

print(queue) # We expect to see Terry and Graham at the end of the queue

print(queue.popleft())                 # The first to arrive now leaves

print(queue.popleft())                 # The second to arrive now leaves

print(queue)                           # Remaining queue in order of arrival

queue.appendleft('John')

print(queue)                           # John is added to start of queue

# We get what we expect! 
```

Here we use `deque.popleft()` to remove from the left and `deque.appendleft()` to add to the left. 

### List Comprehensions

List comprehensions provide a concise way to create lists. The following examples will illustrate the syntax. 

```
# Should produce a list of pairs of elements from both lists that are not equal
list = [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]

print(list)

# Should do the same thing
combs = []

for x in [1,2,3]:
    for y in [3,1,4]:
        if x != y:
            combs.append((x, y))

print(combs)
```

The syntax is that the first element is equivalent to `.append()`. Then we have a necessary `for` statement. Then we can have any sequence of `for` and `if` elements. In the above code we have our appended items being an (x,y) pair, this item is being created from a `for` loop over one list, that then instantiates a `for` loop over another loop, which then adds an item if the `if` condition is satisfied. If the expression is a tuple it must be parenthesized. 

The following gives more examples of what can be done using list comprehension. 

```
vec = [-4, -2, 0, 2, 4]
# create a new list with the values doubled
[x*2 for x in vec]
print(vec)

# filter the list to exclude negative numbers
[x for x in vec if x >= 0]
print(vec)

# apply a function to all the elements
[abs(x) for x in vec]
print(vec)

# call a method on each element
freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
stripped = [weapon.strip() for weapon in freshfruit]
print(stripped)

# create a list of 2-tuples like (number, square)
truth = [(x, x**2) for x in range(6)]
print(truth)

# flatten a list using a listcomp with two 'for'
vec = [[1,2,3], [4,5,6], [7,8,9]]
vec = [num for elem in vec for num in elem]
print(vec)
```

We get nothing out of the ordinary in the above example. We can see that we can use list comprehension for neat unpacking of lists, using nested for loops. We also see that we need to wrap our tuples in parentheses. We also see that we can use functions as the first element in list comprehension, such that the elements added have functions applied to them before they are added (this makes sense as we know the first element in list comprehension is equivalent to `append()`).

### Nested List Comprehensions

One can use a list comprehension as the argument given to the `append()` in another list comprehension. In other words you can do a list comprehension in another list comprenhension. 

### The `del` statement

The `del` statement is like the `remove()` method except it accepts an index rather than a value. It can also be used to delete entire variables, if you want those variables to not be referenced thereafter. 

### Tuples and Sequences

Lists are a sequence data type. The other standard data type in python is tuples. A tuple consists of two values separated by a comma. For example: 

```
t = 12345, 54321, 'hello!'
print(t[0])

print(t)

# Tuples may be nested:
u = t, (1, 2, 3, 4, 5)
print(u)

# but they can contain mutable objects:
v = ([1, 2, 3], [3, 2, 1])
print(v)

# Empty tuples are constructed using empty parentheses
empty = ()
print(empty)
print(len(empty))

# Singleton tuples are constructed using a trailing comma
singleton = 'hello',
print(singleton)
print(len(singleton))
```

We see that tuples are immutable, that they can contain mutable objects like lists, and that they may be nested. We also see that empty tuples are created using empty parentheses, and that singleton tuples are created with a trailing comma. The length of an empty tuple is 0, and the length of a simpleton is 1. 

Though tuples may seem similar to lists, they are often used in different situations and for different purposes. Tuples are immutable, and usually contain a heterogeneous sequence of elements that are accessed via unpacking (see later in this section) or indexing (or even by attribute in the case of namedtuples). Lists are mutable, and their elements are usually homogeneous and are accessed by iterating over the list.

The statement `t = 12345, 54321, 'hello!'` is an example of tuple packing. The reverse could happen if we did `x,y,z = t`

This is called sequence unpacking, and sequence unpacking requires that there are as many variables on the left side of the equals sign as there are elements in the sequence. 

### Sets

A set is an unordered collection with no duplicate elements. Sets can be used to test for membership, and eliminating duplicate entries. Sets also support mathematical operations like union, intersection, difference and symmetric difference. To create an empty set you have to use set(), not {} which creates an empty dictionary. 

```
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)                      # show that duplicates have been removed

print('orange' in basket)               # fast membership testing

print('crabgrass' in basket)

# Demonstrate set operations on unique letters from two words
a = set('abracadabra')
b = set('alacazam')
print(a)                                  # unique letters in a

print(a - b)                           # letters in a but not in b

print(a | b)                              # letters in a or b or both

print(a & b)                             # letters in both a and b

print(a ^ b)                              # letters in a or b but not both
```

Set works the way we expect. The only operation we aren't used to is `^` which is symmetric difference. Set comprehensions are supported. 

### Dictionaries

Dictionaries are sometimes found in other languages as “associative memories” or “associative arrays”. Unlike sequences, which are indexed by a range of numbers, dictionaries are indexed by keys, which can be any immutable type; strings and numbers can always be keys. Tuples can be used as keys if they contain only strings, numbers, or tuples; if a tuple contains any mutable object either directly or indirectly, it cannot be used as a key. Dictionaries are a set of key:value pairs, with the requirement that keys are unique. 

You can delete a key:value pair using the `del` statement. Performing list(d) on a dictionary returns a list of all the keys used in the dictionary, in insertion order. If you want it sorted you use sorted(d). To check whether a single key is in a dictionary use the `in` keyword. 

```
# This should instantiate the dictionary
tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127

print(tel)

print(tel['jack'])

# This should delete the element of the dictionary associated with the key 'sape'
del tel['sape']
tel['irv'] = 4127
print(tel)

# Can use the list statement to transform dictionaries to lists
print(list(tel))

# Should return a sorted list of the keys of our dictionary
print(sorted(tel))

# Should test for dictionary membership for the keys
print('guido' in tel)

print('jack' not in tel)
```

We see that we get the behavior we expect. `sorted(d)` and `list(d)` return lists of keys. We can remove elements using `del` and we can add elements to a dictionary using the syntax shown above: dict['key'] = value. 

The dict() constructor builds dictionaries directly from sequences of key-value pairs:

```
# Should construct a dictionary using the dict function
tel = dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])

print(tel)

# Should construct a dictionary using a dict expression
keys = {x: x**2 for x in (2, 4, 6)}

print(keys)

# When the keys are simple strings it is sometimes easier to specify pairs 
# using keyword arguments
tel = dict(sape=4139, guido=4127, jack=4098)

print(tel)
```

We see we get the behavior we expect, and that we can do dict comprehension. 

### Looping Techniques

When looping through dictionaries the key and corresponding value can be retrieved directly using the items() method:

```
# Dictionary looping
knights = {'gallahad': 'the pure', 'robin': 'the brave'}

# We expect that this will return a list of two place tuples
print(knights.items())

# Should print the successive keys and values in knights
for k, v in knights.items():
    print(type(k))
    print(type(v))
    print(k, v)

# Should print the values of our list, with their keys being 0 through 2
for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)

# Should loop over both lists, where the lists are combined into a list of 
# two place tuples
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']

# Zip is an iterator, so we expect it will return a zip type object
l = zip(questions,answers)

print(l)

for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))

# Reversed should reverse the order of a list (so in this case should return 
# 9 through one, only including odds)
for i in reversed(range(1, 10, 2)):
    print(i)

# Should loop over a sequence in a sorted order, using the sorted() method
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for i in sorted(basket):
    print(i)

# Should print the list in order but without duplicates
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket)):
    print(f)

# The following should return a list without the NaNs
import math
raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
filtered_data = []
for value in raw_data:
    if not math.isnan(value):
        filtered_data.append(value)

print(filtered_data)
```

We see that we get what expect. For lists containing two place tuples, the value that we include before the for loop is a two place tuple, so we can reference both elements of the first value in the list. `items()` returns a list of two place tuples for dictionaries. When creating a new list from an old list, it is advisable to create a new list, set or dictionary, rather than deleting items from the initial list. We should be careful with the `zip()` method, as it returns an iterator to save money. To get a list from `zip()` we would have to do something like `list(zip(arg1,arg2))`

### More on Conditions

The conditions used in `while` and `if` statements can contain any operators, not just comparators. The comparison operators `in` and `not in` are membership tests that determine whether a value is in, or not in a container. The operators `is` and `is not` compare whether two objects are really the same object. All comparison operators have the same priority, which is lower than all numerical operators. For example `a < b == c` tests whether a is less than b, and whether b equals c. Comparison operators may be combined using boolean operators `and`, `or` and `not`. These operators have lower priority than comparison operators, and between them `not` has the highest priority and `or` the lowest. This results in `A and not B or C` being equivalent to `(A and (not B)) or C`. As always parentheses can be used to express the desired composition. 

The boolean operators `and` and `or` are so called short circuit operators. Their arguments are evaluated from left to right, and evaluations stops as soon as an outcome is determined. When used as a general value and not a Boolean the returned value is the last evaluated argument. It is possible to assign the result of a comparison or other Boolean expression to a variable. For example:

```
# We expect the following to assign 'Trondheim' to non_null
string1, string2, string3 = '', 'Trondheim', 'Hammer Dance'
non_null = string1 or string2 or string3
print(non_null)
```

We see we get what we expect. 

In Python, unlike C, assignment inside expressions must be done explicitly with the walrus operator `:=`. This avoids typing `=` when `==` was intended. 

### Comparing Sequences to other Types 

Sequence objects may typically be compared to other objects of the same sequence type. The comparison uses *lexicographical* ordering. First the first two items are compared, and if they differ this determines the outcome of the comparison; if they are equal, the next two items are compared, and so on, until either sequence is exhausted. If the two items to be compared are themselves sequences of the same type, the *lexicographical* comparison is carried out recursively. If all items of two sequences compare equal, the sequences are considered equal. If one sequence is an initial sub-sequence of the other, the shorter sequence is the smaller (lesser) one. Lexicographical ordering for strings uses the Unicode code point number to order individual characters. Some examples of comparisons between sequences of the same type:

```
# We expect the following to be true
comp1 = ((1, 2, 3) < (1, 2, 4))
print(comp1)

# We expect the following to be true
comp2 = ([1, 2, 3] < [1, 2, 4])
print(comp2)

# We expect the following to be true
comp3 = ('ABC' < 'C' < 'Pascal' < 'Python')
print(comp3)

# We expect the following to be true
comp4 = ((1, 2, 3, 4) < (1, 2, 4))
print(comp4)

# We expect the following to be true
comp5 = ((1, 2) < (1, 2, -1))
print(comp5)

# We expect the following to be true
comp6 = ((1, 2, 3) == (1.0, 2.0, 3.0))
print(comp6)

# We expect the following to be true
comp7 = ((1, 2, ('aa', 'ab')) < (1, 2, ('abc', 'a'), 4))
print(comp7)
```

We get what we expect! We see that the comparison stops once an order has been decided. We see that strict substrings are considered less than. We see that comparison of strings goes by Unicode point number, and therefore alphabetical order, and we see that recursive *lexicographical* comparison works. We note that we can compare objects of different types, so long as we have appropriate comparison methods (so floats and ints are fair game, but floats and strings aren't). 

## Module 6 - Modules

