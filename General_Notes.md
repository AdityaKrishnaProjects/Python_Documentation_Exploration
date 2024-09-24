## Preface

This file will serve as my general notes on the python documentation. The headings of this markdown file will correspond to the different chapters in the table of contents for Python Documentation as of September 2024, starting on Module 3. Within this note I will reference the modules and experiments I did with them, the code for these modules I experimented with and the results of these experiments will be housed in the modules folder.

### Module 3 - An Informal Introduction to Python

__Basics__

In python everything is an object. When we declare a variable, we are really binding a name to an object. From then on this name will be used to refer to this object. 

__Experiments with names and binding__

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

__Strings and basic string functions__

Strings are stored as lists, and so you can reference their entries as you would in a list. Strings are immutable so you can not edit them like normal lists. 

__Splicing__

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

__Lists__

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

__Indentation__

This is critically important to the syntax of python. Indentation is python's way of grouping statements. The body of any control flow operator will be indented. 

__Appendix__

You can assign multiple variables in one line in python 

```
a, b = 1, 2
```

This will give us a = 1 and b = 2. Python evaluates the right hand side first, and it reads the right hand side from left to right (which is perfect as we can have operations complete on the righthand side before assignment to a name, and these operations will occur in an expected order of operations).

In python any non-zero integer value is true, whereas zero is false. In any sequence anything with a non-zero length is true, whereas empty sequences are false. 

### Module 4 - More Control Flow Tools

__if Statements__

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

__Indentation for Control Flow__

It is important to realise that indentation gives the control flow operator the instructions for what to do if its condition is met. With this in mind, it makes sense that the else operator is on the same line as the if operator, as if it was inside of the body of if, then else would execute after if executed, whereas we know they represent two different paths for execution of the program. This is why elif is useful, as without if the new if would be in the body of else, and then we would get cascading else operators for multiple cases. For comparing the same value to several constants or checking for specific types or attributes we might use the match statement. 

__for Statements__

__Seeing how for loops over strings works__

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

__range()__

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

__break__

