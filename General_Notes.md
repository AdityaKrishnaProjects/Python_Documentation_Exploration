#### Preface

This file will serve as my general notes on the python documentation. The headings of this markdown file will correspond to the different chapters in the table of contents for Python Documentation as of September 2024, starting on Module 4. Within this note I will reference the modules and experiments I did with them, the code for these modules I experimented with and the results of these experiments will be housed in the modules folder.

##### Module 4 - More Control Flow Tools

*if Statements*

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

elif is used in place of doing an else and then an indented if after if statements to avoid excessive indentation statements with further if statments.

*for Statements*

*Seeing how for loops over strings works*

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

