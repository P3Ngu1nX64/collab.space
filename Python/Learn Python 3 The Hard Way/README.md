# Learn Python 3 the Hard Way
### __Python Learning - collab.space__

The primary instruction resource is based on a PDF extraction of a book and online HTML webpage tutorial by the author __Zed Shaw__.
collab.space in no way takes credit for the uploaded PDF. It is courtesy of [learnpythonthehardway.org](https://learnpythonthehardway.org/python3/), and it is incorporated into this GitHub directory solely for the purpose of reference.


## Exercises
The following section will be concerned with the exercises of the tutorial: Learn Python 3 the Hard Way. It includes annotations of the self-explanatory tutorial rather than explanations.
Disclaimer: The set up process is very sophisticated, along with its Command Line Crash Course (in the appendix, page 288), could be put into a separate tutorial. Therefore, it will not be incorporated into this tutorial. Therefore, our first exercise will be on Page 34 of the PDF.
Here is a short Table of Contents.

Exercise No# | Exercise Name | Page Number
---:|---|:---:
1 | A Good First Program | 34
2 | Comments and Pound Characters | 40
3 | Numbers and Math | 42
4 | Variable and Names | 46
5 | More Variables and Printing | 50
6 | Strings and Text | 52
7 | More Printing | 56
8 | Printing, Printing | 60
9 | Printing, Printing, Printing | 62
10 | What Was That? | 64
11 | Asking Questions | 68
12 | Prompting People | 70
13 | Parameters, Unpacking, Variables | 72
14 | Prompting and Passing | 76
15 | Reading Files | 80
16 | Reading and Writing Files | 84
17 | More Files | 88
18 | Names, Variables, Code, Functions | 92
19 | Functions and Variables | 96
20 | Functions and Files | 100
21 | Functions Can Return Something | 104
22 | What Do You Know So Far? | 108
23 | Strings, Bytes, and Character Encodings | 110
24 | More Practice | 118
25 | Even More Practice | 112
26 | Congratulations, Take a Test! | 126
27 | Memorizing Logic | 128
28 | Boolean Practice | 132
29 | What If | 136
30 | Else and If | 138
31 | Making Decisions | 142
32 | Loops and Lists | 146
33 | While Loops | 150
34 | Accessing Elements of Lists | 154
35 | Branches and Functions | 156
36 | Designing and Debugging | 160
37 | Symbol Review | 162
38 | Doing Things to Lists | 168
39 | Dictionaries, Oh Lovely Dictionaries | 174
40 | Modules, Classes, and Objects | 180
41 | Learning to Speak Object-Oriented | 186
42 | Is-A, Has-A, Objects, and Classes | 192
43 | Basic Object-Oriented Analysis and Design | 198
44 | Inheritance Versus Composition | 214
45 | You Make a Game | 224
46 | A Project Skeleton | 228
47 | Automated Testing | 236
48 | Advanced User Input | 240
49 | Making Sentences | 248
50 | Your First Website | 256
51 | Getting Input from a Browser | 264
52 | The Start of Your Web Game | 274

_52/52 exercises uploaded_

Notes:
* ex37: Draw.io is used to create flowcharts. The file 'Python Default Flowchart Template.drawio' is a template for writing flowcharts for Python. When adding flowcharts, both the .drawio file and the exported file will be added to GitHub.

Todos:
- [x] Figure out Exercise 23 "Very Difficult" Challenge (still a no :confused:) <–– NVM I think I figured it out <–– Update! I did! :rofl:
- [ ] Change/Format all ex_information.txt files to .md files.
- [x] Finish Exercises 1-26 (Beginner)
- [x] Finish Exercises 27-44 (Intermediate)
- [ ] Finish Exercises 45-52 (Advanced)
- [ ] Add attributions to Zed Shaw in each exercise file.
- [x] More markdown integration! @stephi8013
  - [ ] Write an explanatory README.md File for each Exercise/Folder
  - [ ] Write a collective markdown file as a recap for everything (concise and helpful).

# Summary

Here is a Summary of each exercise, made as concise as possible while covering key points from the exercises.

### Exercise 1

Print text to the console using `print()`

A `str` or String is a sequence of characters placed within quotes (e.g. `"Hello, world"`).

- Inside apostrophes `' '` (single quotes), double quotes are ignored.
- Inside double quotes `" "`, apostrophes (single quotes) are ignored.

So this would be valid

```python
In[1]: print("I didn't")
In[2]: print('he said "go over there"')
```

```
Out[1]: I didn't
Out[2]: he said "go over there"
```

### Exercise 2

A # (called Octothrope, Pound, Hash, or Mesh.) is a comment

Code after a comment on the same line will not be executed by the compiler.

Comments could be put at the end of a line of code.

```python
print("Hello, world!")  # And here is a comment
```

### Exercise 3

Basic Arithmetic Operators

Operand Name | Operand | Purpose
:-|:-:|:-
Plus | `+` | Addition
Minus | `-` | Subtraction
Slash | `/` | Division
Double Slash | `//` | Floor Division – Quotient w/o Remainder
Asterisk | `*` | Multiplication
Double Asterisk | `**` | Exponentiation
Percent | `%` | Modulo (?)
Less-than | `<` | Comparison Smaller
Greater-than | `>` | Comparison Larger
Less-than-equal | `<=` | Comparison Smaller or Equivalent
Greater-than-equal | `>=` | Comparison Larger or Equivalent

Operands can be used inside functions, equivalence operators returns a Boolean (`True` or `False`) value.

Inside `print()`, a Plus `+` concatenates while a Comma `,` interpolates strings.

```python
In[1]: print("Is 3+2 greater than 6?", 3 + 2 > 6)
In[2]: print("What is 3+4?", 3 + 4)
```

```
Out[1]: Is 3+2 greater than 6? False
Out[2]: What is 3+4? 7
```

### Exercise 4

Variables could be assigned. Their definition syntax is `name = value` where name is the name of the variable and value is the data assigned to the value.

An `int` is an integer (e.g. `1`), while a `float` is a floating decimal number (e.g. `0.1`)

### Exercise 5

F-strings are one of the ways to fill in strings with other values. An F-string is just a string with the character `f` in front of the quotes. Inside an F-string, curly brackets `{}` store variables (or other values).

```python
In[1]: greeting = "Hello World"
In[2]: first_number = 4
In[3]: second_number = 5
In[4]: print(f"{greeting}! The sum of {first_number} and {second_number} is {first_number + second_number}.")
```

```
Out[1]: Hello World! The sum of 4 and 5 is 9.
```

### Exercise 6

The other way to format a string is by calling the `.format()` method on the string. This allows template strings to be stored inside variables, and formatted when called.

```python
In[1]: template = "There once was a {} who {}."
In[2]: print(template.format('boy', 'skates'))
In[3]: print("Hello there, {}!".format("David"))
```

```
Out[2]: There once was a boy who skates.
Out[3]: Hello there, David!
```

### Exercise 7

In python, a shorthand for concatenating a string upon itself any number of times can be achieved with the asterisk `*`.

To prevent the `print()` function from causing a new line (_by default_) at the end of the printed string, specify `end=''` or any other specification at the end of the print function.

```python
In[1]: print('-' * 10, end=', ')
In[2]: print(('<' + '>') * 10)
```

```
Out[1 and 2]: ----------, <><><><><><><><><><>
```

### Exercise 8

For template `.format()` strings, Refer to Exercise 6

### Exercise 9

Triple quotes can extend between lines. They have other uses as well (as comments and documentation for module functions). There are triple apostrophes `''' '''` and triple quotes `""" """`.

```python
In[1]: text = '''Hello,
>World
>!!!'''
In[2] print(text)
In[3] print("""Print
>Multiline
>Text.""")
```

```
Out[2]: Hello,
        World
        !!!
Out[3]: Print
        Multiline
        Text.
```

For escape sequences, Refer to Exercise 10.

### Exercise 10

In python, there are escape sequences for some special characters, including tabs and newlines.

```python
In[1]: tabbed = "\tTabbed Text."
In[2]: print(tabbed)
In[3]: print("Useful\nText\nWith\nNewlines.")
```

```
Out[2]:     Tabbed Text.
Out[3]: Useful
        Text
        With
        Newlines.
```

List of Escape Sequences

Sequence | Description
:-:|:-
`\\`|Returns \
`\'`|Returns '
`\"`|Returns "
`\a`|Returns ASCII bell (BEL)
`\b`|Returns ASCII backspace (BS)
`\f`|Returns ASCII formfeed (FF)
`\n`|Returns ASCII linefeed (LF)
`\N{name}`|Returns Character named name in the Unicode Database only
`\r`|Carriage Return (CR)
`\t`|Horizontal tab (TAB)
`\uxxxx`|Character with 16-bit hex value xxxx
`\Uxxxxxxxx`|Character with 32-bit hex value xxxxxxxx
`\v`|ASCII vertical tab (VT)
`\ooo`|Character with octal value ooo
`\xhh`|Character with hex value hh

### Exercise 11

The function `input()` prompts the console for input and returns it as a string. The input takes a string parameter to be the prompt.

```python
In[1]: input_text = input()
In[2]: name = input("What's Your Name?\n")
In[3]: print(f"Hi {name}, you said \"{input_text}\"")
```

_Note_: The input is typed in by the user.

```
Out[1]: Hello, world!
Out[2]: What's Your Name?
        Tom
Out[3]: Hi Tom, you said "Hello, world!"
```

### Exercise 12

For the function `input()`, Refer to Exercise 11.

For f-strings, Refer to Exercise 5.

### Exercise 13

`argv` is a `sys` System module that checks for input argument when executing the script, the parameters, unless enclosed as a string, are separated via spaces. `argv` is a list with the user inputs in order.

To use `argv`, it has to be imported first, as with all other packages. In this case, it is imported from the `sys` module.

```python
In[1]: from sys import argv
In[2]: script, first, second, third = argv
In[3]: print("The script is called: ", script)
In[4]: print("Your first variable is: ", first)
In[5]: print("Your second variable is: ", second)
In[6]: print("Your third variable is: ", third)
```

In line 2, we also see another way of unpacking lists: by assigning each index of a list a variable in order.

Programs like these cannot be run directly in the IDE, which cannot pass arguments when executing a file. They have to be run in a shell (denoted with a `$` sign)

```
$ python3 ex13.py Uno Zwei Trois
Out[3]: The script is called: ex13.py
Out[4]: Your first variable is: Uno
Out[5]: Your second variable is: Zwei
Out[6]: Your third variable is: Trois
```

### Exercise 14

For the function `input()`, Refer to Exercise 11.

For the module `argv`, Refer to Exercise 13.

### Exercise 15

To open a file, you will have to call the `open()` function.

It is easiest to manipulate a file by assigning its open object to a variable. After it is assigned, you can read the file from the variable. When finished, make sure that the file is formally closed within the program.

When opening files, always specify permissions as a positional argument after the file path. 'r' is for read, 'a' is for append, and 'w' is for write (will truncate file), add a 'b' behind any of those three for reading and modifying binary files.

_Assuming there is a text file named "sample.txt" in the current working directory,_

```python
In[1]: filepath = "sample.txt"
In[2]: file = open(filepath, 'r')  # Could also do: file = open("sample.txt", 'r')
In[3]: print(file.read())
In[4]: file.close()
```

```
Out[3]: File Contents Listed Here
```

### Exercise 16

For file modes and permissions, Refer to Exercise 15 (and binary mode)

Mode | Permissions
:-:|:-
`'r'` | Read: can only read the file
`'a'` | Append: can only append to a file (writable seek always at EOF) *
`'w'` | Write: can write and truncate a file *
`'r+'` | Can read and write
`'a+'` | Can read, and write only at end of file *
`'w+'` | Can read and write *

_\*: Creates file if it doesn't exist_

File actions:

Method | Description
:-:|:-
`file.close()` | Saves and Closes file 'x'.
`file.read()` | Reads content of file/variable 'x' and returns result.
`file.readline()` | Reads and returns just one line of file (with defining parameter).
`file.truncate()` | Empties (and removes) contents of file 'x' (Beware!).
`file.write(content)` | Writes content to file.
`x.seek(0)` | Moves the read/write location to the beginning of file 'x'.
`x.seek(n)` | Moves the read/write location to the nth character of file 'x'.

### Exercise 17

For file actions/methods, Refer to Exercise 16.

Example: Make a copy of a file in one line given `from_file` and `to_file`

```python
out_file = open(to_file, 'w').write(open(from_file).read())
```

### Exercise 18

Functions are initiated with `def` and can perform actions and return values. Functions are mostly used to reduce repetitiveness in code. A function is "_called_" when it is used.

```python
In[1]: def print_two(arg1, arg2):
>          print(f"arg1: {arg1}, arg2: {arg2}")
In[2]: print_two("Apple", "Banana")
```

```
Out[2]: arg1: Apple, arg2: Banana
```

_Note_: Refer to Function Checklist for reminders when calling and defining functions.

### Exercise 19

For functions, Refer to Exercise 18

For number datatypes and arithmetic operators, Refer to Exercise 3

### Exercise 20

For functions, Refer to Exercise 18

For file actions/methods, refer to Exercise 16

### Exercise 21

Same as Exercise 19

### Exercise 22 (Review)

### Exercise 23

Concept: UTF-8 is an ASCII format that "_escapes_" to unicode (a larger, space consuming format with more symbols from other languages and emojis).

Mnemonic: "**DBES**" **Decode Bytes, Encode Strings**. **Decode** bytes in a alphanumerically (_ASCII_) represented binary format to get **Strings**, **Encode** strings to store them as **Bytes**.

In Python, the datatype _bytes_ are represented by an enclosing `b' '`. Type `byte` has the method `.decode(encoding=utf-8, errors=strict)` (where you can change the arguments from the defaults by specifically referencing them) and type `str` has the method `.encode(encoding=utf-8, errors=strict)`

There are a few more self explanatory methods to data encoding that will be presented in the examples. Refer to the exercise for greater detail.

```python
# ASCII
In[1]: print(0b1011010)
Out[1]: 90

In[2]: print(format(90, 'b'))
Out[2]: 1011010

In[3]: print(int(1011010, 2))
Out[3]: 90

In[4]: ord('Z')
Out[4]: 90

In[5]: chr(90)
Out[5]: 'Z'

# UNICODE
In[6]: ord('')
Out[6]: 63743

In[7]: chr(63743)
Out[7]: ''

In[8]: to_encode = ''

In[9]: print(to_encode.encode(encoding=utf-8, errors=strict))
Out[9]: b'\xef\xa3\xbf'

In[10]: to_decode = b'\xef\xa3\xbf'

In[11]: print(to_decode.decode(encoding=utf-8, errors=strict))
Out[11]: ''

In[12]: print(type(to_decode))
Out[12]: <class 'bytes'>
```

### Exercise 24

Same as 19.

### Exercise 25

[List Operations](https://docs.python.org/3/tutorial/datastructures.html)

In Python, lists are defined using square brackets `[]`. They can comprise of any mix of data types, and they are _mutable_

Method | Description | Equivalent to
:-:|:-|:-:
`list.append(x)` | Add an item to the end of the list. | `a[len(a):] = [x]`
`list.extend(iterable)` | Extend the list by appending all the items from the iterable. | `a[len(a):] = iterable`
`list.insert(i, x)` | inserts item x to position/index i | E.g. `a.insert(len(a), x)` = `a.append(x)`
`list.remove(x)` | Remove the first item from the list whose value is equal to x, ValueError if not x in list. |
`list.pop([i])` | Remove the item at the given position in the list, and return it. If no index is specified, `a.pop()` removes and returns the last item in the list. | E.g. `list.pop(0)` = `list.popleft()`
`list.clear()` | Remove all items from the list. | `del a[:]`
`list.index(x[, start[, end]])` | Return zero-based index in the list of the first item whose value is equal to x. Raises ValueError if not x in list. |
`list.count(x)` | Return the number of times x appears in the list. |
`list.sort(key=None, reverse=False)` | Sort the items of the list in place (the arguments can be used for sort customization |
`list.reverse()` | Reverse the elements of the list in place.
`list.copy()` | Return a shallow copy of the list. | `a[:]`

_Notes:_
- `list.insert(0, x)` inserts x to the start of the list
- The square brackets around the i in the method signature of `list.pop()` denote that the parameter is optional, not that you should type square brackets at that position. You will see this notation frequently in the Python Library Reference.
- See [`sorted()`](https://docs.python.org/3/library/functions.html#sorted) for the explanation of the sorting arguments of method `list.sort()`

### Exercise 26 (Test)

### Exercise 27

This Exercise is about Logic and Truth Values (Conditionals)

Truth Terms:

<b>
* and
* or
* not
* != (not equal)
* == (equal)
* \>= (greater-than-equal)
* <= (less-than-equal)
* True
* False
</b>

Important Truth Tables to Remember:

<center>

**NOT** | **True?**
:---:|:---
_not_ False | True
_not_ True | False

**OR** | **True?**
:---:|:---
True _or_ True | True
True _or_ False | True
False _or_ True | True
False _or_ False | False

**AND** | **True?**
:---:|:---
True _and_ True | True
True _and_ False | False
False _and_ True | False
False _and_ False | False

_popularly referred to as **NOR**_

**NOT OR** | **True?**
:---:|:---
_not_ (True _or_ True) | False
_not_ (True _or_ False) | False
_not_ (False _or_ True) | False
_not_ (False _or_ False) | True

_popularly referred to as **NAND**_

**NOT AND** | **True?**
:---:|:---
_not_ (True _and_ True) | False
_not_ (True _and_ False) | True
_not_ (False _and_ True) | True
_not_ (False _and_ False) | True


And two more charts dealing with equality:

**!=** | **True?**
:---:|:---
1 != 1 | False
1 != 0 | True
0 != 1 | True
0 != 0 | False

**==** | **True?**
:---:|:---
1 == 1 | True
1 == 0 | False
0 == 1 | False
0 == 0 | True

</center>

### Exercise 28

Equality Operators:

Operator | Name | Description
:-:|:-|:-
`==` | equal | If the values of two operands are equal, then the condition becomes true.
`!=` | unequal | If values of two operands are not equal, then condition becomes true.
`>` | greater-than | If the value of left operand is greater than the value of right operand, then condition becomes true.
`<` | less-than | If the value of left operand is less than the value of right operand, then condition becomes true.
`>=` | greater-than-equal | If the value of left operand is greater than or equal to the value of right operand, then condition becomes true.
`<=` | less-than-equal | If the value of left operand is less than or equal to the value of right operand, then condition becomes true.

Binary Operators:

Operator | Name | Description
:-:|:-|:-
`&` | Binary AND | Operator copies a bit to the result if it exists in both operands
`|` | Binary OR | It copies a bit if it exists in either operand.
`^` | Binary XOR | It copies the bit only if it is set in one operand and not both.
`~` | Binary Ones Complacent | It is unary and has the effect of 'flipping' bits.
`<<` | Binary Shift Left | The left operands value is moved left by the number of bits specified by the right operand. (This numerically multiplies by 2 per digit moved)
`>>` | Binary Shift Right | The left operands value is moved right by the number of bits specified by the right operand. (This numerically divides by 2 per digit moved)

### Exercise 29

If Statements Syntax should look something like this:

```python
if conditional:
    action
elif conditional:
    action
elif conditional:
    action
else:
    action
```

As many `elif` else if blocks can be nested as needed. `action`s are commands that are executed if their `conditional` is `True`. The if statements are executed **in order**, meaning that if more than one `conditional` is True, the first one in order will be executed.

### Exercise 30

For if-statements, Refer to Exercise 29.

### Exercise 31

Same as 30 and 19.

_Note_: `sys.exit()` is a System Module that quits a script. It takes an input (most commonly a number) as an exit code. `0` means no errors have occurred, that it is just a normal part of the script. While other cardinals refer to some sort of error.

### Exercise 32

For lists, Refer to Exercise 25.

**For Loops** are the most intuitive loops. They iterate something some number of times while executing the code block within itself each iteration. It is better to think of for loops as iterating lists, as the for loop can also iterate through values in a list. Their basic syntax is as follows.

```python
for range:
    actions

for value in list:
    actions(value)
```

The `range()` function takes two arguments, start and stop: `range(start, stop)`. It will describe the range [start, stop), more specifically for integers: [start, stop - 1]

In the second example, value is equivalent to the value of the list at the index that is currently being iterated.

List Unpacking Reminder: `*list` will unpack the contents of list one by one (as an _iterable_).

### Exercise 33

For for loops, Refer to Exercise 32.

### Exercise 34

For lists, Refer to Exercise 25.

For for loops, Refer to Exercise 32.

### Exercise 35

same as 34, 30, and 19.

### Exercise 36 (Writing Practice)

For flow charts, Ref#!

### Exercise 37 (Review)

Data Types:

Type | Description | Example
:-:|:-|:-
bytes | Stores bytes, maybe of text, PNG, file, etc. | `x = b"hello"`
dicts | Stores a key=value mapping of things. | `e = {'x': 1, 'y': 2}`
False | False boolean value. | `False and True == False`
floats | Stores decimals. | `i = 10.389`
lists | Stores a list of things. | `j = [1,2,3,4]`
None | Represents ”nothing” or ”no value”. | `x = None`
numbers | Stores integers. | `i = 100`
strings | Stores textual information. | `x = "hello"`
True | True boolean value. | `True or False == True`

Old (Python 2) String Formats (using %)

Escape | Description | Example
:-:|:-|:-
`%%` | A percent sign. | `"%g%%" % 10.34 == '10.34%'"`
`%c` | Character format. | `"%c" % 34 == '"'`
`%d` | Decimal integers (not floating point). | `"%d" % 45 == '45'`
`%e` | Exponential notation, lowercase ’e’. | `"%e" % 1000 == '1.000000e+03'`
`%E` | Exponential notation, uppercase ’E’. | `"%E" % 1000 == '1.000000E+03'`
`%f` | Floating point real number. | `"%f" % 10.34 == '10.340000'`
`%F` | Same as %f. | `"%F" % 10.34 == '10.340000'`
`%g` | "Either %f or %e, whichever is shorter. | `%g" % 10.34 == '10.34'`
`%G` | Same as %g but uppercase. | `"%G" % 10.34 == '10.34'`
`%i` | Same as %d. | `"%i" % 45 == '45'`
`%o` | Octal number. | `"%o" % 1000 == '1750'`
`%r` | Repr format (debugging format). | `"%r" % int == "<type 'int'>"`
`%s` | String format. | `"%s there" % 'hi' == 'hi there'"`
`%u` | Unsigned decimal. | `"%u" % -1000 == '-1000'"`
`%x` | Hexadecimal lowercase. | `"%x" % 1000 == '3e8'`
`%X` | Hexadecimal uppercase. | `"%X" % 1000 == '3E8'`


Special (somewhat uncommon) Operators:

Operator | Description | Example
:-:|:-|:-
`+=` | Add and assign | `x = 1; x += 2`
`@` | At (decorators) | `@classmethod`
`/=` | Divide and assign | `x = 10; x /= 2; x == 5`
`==` | Equal | `4 == 5 == False`
`//=` | Floor divide and assign | `x = 24; x //= 4; x == 1`
`//` | Floor division | `9 // 5 == 0`
`%=` | Modulus assign | `x = 99; x %= 20; x == 19`
`*=` | Multiply and assign | `x = 5; x *= 2; x == 10`
`!=` | Not equal | `4 != 5 == True`
`**=` | Power assign | `x = 5; x **= 3; x == 125`
`**` | Power of | `2 ** 4 == 16`
`%` | String interpolate or modulus | `2 % 4 == 2`
`-=` | Subtract and assign | `x = 1; x -= 2; x == -1`

Interesting Functions:
_The use of these functions were not explicitly referred to in the book. Reference links will be included for all of them_

Function | Short Description
:-:|:-
[`break`][pydoc_break_continue] | Breaks out of the innermost enclosing for or while loop. Will nullify the loops else statement, if any.
[`continue`][pydoc_break_continue] | Skip to the next iteration (if applicable) of a loop without processing more of the current iteration.
[`compile()`][pydoc_compile] | Compiles larger chunks of code for evaluation.
[`eval()`][pydoc_eval] | Evaluates a single expression.
[`exec()`][pydoc_exec] | Evaluates one "line"/block of code.
[`global`][pydoc_global] | Allows modification of a variable from a module-level scope. Avoids UnboundLocalError, placed inside local scopes.
[`lambda`][resource_lambda] | Creates an anonymous function, can only have one expression that is returned. Examples: `lambda arguments: expression`. Can be used as a function object by defining it equal to a variable or input when a function is required as an argument.
[`nonlocal`][pydoc_nonlocal] | Allows modification of a variable from a scope that is one higher its current.
[`pass`][pydoc_pass] | A placeholder for a function/class without actions/methods yet.
[`raise`][pydoc_raise] | Raises an exception (error) when things go wrong.
[`try: except: else: finally:`][pydoc_try] | Tries a block, Except handles errors in python from a Try block, Else is triggered when Try fails, and Finally is the cleanup block that gets executed regardless.
[`with-as:`][pydoc_with_as] | A convenient code block that makes cleanup easier with error/exception handling, and automatically closing opened files.
[`yield:`][pydoc_yield] | Returns a value to the caller. Good for iterating over large amounts of value one at a time without caching all the data in RAM. A function using yield within its definition is a **generator** function.


<!--References:-->
[pydoc_break_continue]: https://docs.python.org/3/tutorial/controlflow.html#break-and-continue-statements-and-else-clauses-on-loops
[pydoc_compile]: https://docs.python.org/3/library/functions.html#compile
[pydoc_eval]: https://docs.python.org/3/library/functions.html#eval
[pydoc_exec]: https://docs.python.org/3/library/functions.html#exec
[pydoc_global]: https://docs.python.org/3/reference/simple_stmts.html#grammar-token-global-stmt
[resource_lambda]: https://www.programiz.com/python-programming/anonymous-function
[pydoc_nonlocal]: https://docs.python.org/3.2/reference/simple_stmts.html#grammar-token-nonlocal_stmt
[pydoc_pass]: https://docs.python.org/3.2/reference/simple_stmts.html#the-pass-statement
[pydoc_raise]: https://docs.python.org/3/tutorial/errors.html#raising-exceptions
[pydoc_try]: https://docs.python.org/3/reference/compound_stmts.html#the-try-statement
[pydoc_with_as]: https://docs.python.org/3/reference/compound_stmts.html#the-with-statement
[pydoc_yield]: https://docs.python.org/3/reference/expressions.html#yield-expressions
<!--Scopes REF: https://www.programiz.com/python-programming/global-local-nonlocal-variables-->

_Notes_:
- Unlike an if-statement's `else` clause, which runs when none of the above conditions are met, a `try` statement's `else` clause runs when no exceptions are raised, a `for` loop's `else` clause runs when no breaks occur.
- In a function, if a `finally` clause specifies a return value, that will always be returned.

### Exercise 38

For lists, Refer to Exercise 25.

_Note_: Check here for [how bracket slices work](https://python-reference.readthedocs.io/en/latest/docs/brackets/slicing.html).

Syntax: `sequence [start:stop[:step]]` Where start and stop are indices using 0-indexing (starting from 0) and step defaults to 1.

### Exercise 39

In Python, a dictionary is defined using the curly brackets `{}`
