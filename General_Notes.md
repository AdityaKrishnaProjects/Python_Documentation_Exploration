#### Preface

This file will serve as my general notes on the python documentation. The headings of this markdown file will correspond to the different chapters in the table of contents for Python Documentation as of September 2024, starting on Module 4. Within this note I will reference the modules and experiments I did with them, the code for these modules I experimented with and the results of these experiments will be housed in the modules folder.

##### Module 4 - More Control Flow Tools

```
# Seeing how for loops over strings works

test_String = "string"

for letter in test_String:
   print(letter, len(letter))

# Iterates over each character as an element of a string, also worth knowing that strings are immutable, so no use iterating over them to try to change letters
```