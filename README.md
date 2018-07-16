Basics
======

* **Data Objects** int, float, bool, NoneType (scalar primitives).
* **Expression** putting data objects together using operators.
* **Keyword** conveys special meaning to the compiler and/or interpreter.
* **Statements** : expression(s) + keyword(s). Dictates logic.
* **Block** logically grouping multiple statements together.
* **Syntax** expression/statement constructed in valid ways. 
* **Semantic** expression/statement are logical.
* **Variable** named memory location to store data object. A level of abstraction.
* **Binding** first evaulate right side expression then bind to name on left side
* **Assignment operators** (=) used to make variable-value binding/assignment 
* **Arithematic operators** (+, -, \*, /) doing mathematical calculations.
* **Comparison operators** (>, <, == , <=, >=) writing boolen expression.
* **Logical operators** (and, or, not) to combine boolean expression(s).
* **Control Flow** the order in which statements are executed.

If-elif-else (Conditional Control Flow)
=======================================

* SYNTAX :
```python
if <boolean expression(s)>:
    ...statements...
elif <boolen expression(s)>:
    ...statements...
else:
    ...statements...
```

* Whichever `boolean expression(s)` evaluate to True FIRST, only those 
`...statements...` are executed and control moves after the else block. If no 
expression evaluates to True then the statements in `else` block is executed

* Checking of `boolean expression(s)` is sequential. `if` condition checked first. If it
is false then next `elif` below it is checked. If that is false then next `elif` and so on.
If any true condition is encountered during this sequential execution, that block is 
executed and control is transfered to the code after the else block.

Strings
=======

* **String** - sequence of (case-sensitive) characters (NON-SCALAR primitive).

* **Index** is the sequential number assigned to each character in the string

* **String operators** "+" string concatination, "\*" multiple concatinations.
("+" and "\*" are overloaded) type of oparand tells operator what to do. >, <, == 
used to compare string (lexicographically).

* There are many built-in string methods like `append`, `pop`, `indexOf` etc.
* `len(<string>)` : returns number of characters.
* `<string>[index]` : return element at index `index`
* `<string>[start_index:end_index:step]` : slicing of string/substring

I/O operations
==============
* `print("Hello World")` prints to monitor/console.
* `input("prompt")`console input as a string. Input into environment.
* use case
```python
name = input("Enter your name :")
print("Hello {}!".format(name))
```

For loop and while loop (Iterative Control Flow)
================================================

* while-loop SYNTAX : 
```python
while <boolean expression(s)>:
    ...statements...
```
The `...statements...` are repeatedly executed as long as the `boolean expression(s)`
evaluate to true.

* for-loop SYNTAX :
```python
for <variable> in <iterable/generator>:
    ...statements...
```

* `iterable` is a kind of compound data object with various primitive components.
important example : list, tuple, dictionary (keys) etc.
* `generator` is a function that "temporarily return" a value that can be used in 
the iteration. The next time this function is called, operations resume after the
point of "temporarily return".
* `range()` is an in-build generator used to perform loop a fixed number of times
* "variable" = "looping variable". Update looping variable (involed in the boolean 
expression) in while-loop to ensure loop terminates

Jump statements (Variable Control Flow)
=======================================

* `break` terminates loop. Moves control outside loop.
* `continue` abandons current iteration and moves to next iteration
* Making a **function call** with `return` keyword
SYNTAX:
```python
def <called_function>(<formal parameters>)
    ..statements...
    return <value>

def <calling_function>(<parameters>)
    ..statements...
    <variable> = <called_function>(<actual parameters>)
    ..statements...
```
stops current function, creates a new frame for `<called_function>` and sends 
parameter value(s) in this frame (look out for **call by reference**
vs **call by value** differences.)
* **call by reference** address(es) copied from `<actual parameters>` to `<formal parameters>`
* **call by value** value(s) copied from `<actual parameters>` to `<formal parameters>`

* `return` terminates call. deletes `<called_function>`'s frame. sends `<value>` back to the 
`<calling_function>` stores it in `<variable>` and returns control back to the calling function.

* Making a **function call** with `yield` keyword
SYNTAX:
```python
def <called_function>(<formal parameters>)
    ..statements...
    yield <value1>
    ..statements...
    yield <value2>

def <calling_function>(<parameters>)
    ..statements...
    <variable> = <called_function>(<actual parameters>)
    ..statements...
    <variable> = <called_function>(<actual parameters>)
```

* `yield` abandons current call. but frame is not deleted. Sends `<value>` back to the 
`<calling_function>` stores it in `<variable>`. When `<called_function>` is called again
`<called_function>` resumes operation from after the `yield` statement. Example, after 
first call value of `<variable>` is `value1`. After second call its value is `value2`

Terminology & Components
========================

* **Distribution** set of python packages/modules pre-installed along with python
most popular distribution is Anaconda.

* **Environment** Contains the interpreter and user selected extrnal packages/modules. 
Code is loaded into the environment where it is interpreted and any reference to any 
external package/module is resolved. Anaconda comes with a `base` environment.

* **Package Manager** used to download/include packages into currently active environment.
python comes by default with `pip`. Anaconda comes with `conda`.

* **Python shell** where code is run/interpreted in an environment (Anaconda base environment)

* **Package** modules together form a package. can to imported to other piece of code.

* **Module** is simply a `.py file` that is imported by some other `.py file`.

* **.py file** python code is stored in a `.py file`. We can run this code by loading it the 
`python shell` or can use the `import` keyword and use this code within another `.py file`

* **Source code** or simply 'code' is a bunch of expressions/"blocks of code"/functions.

* **Functions** enforce a lot of concepts of good programming like (encapsulation. abstraction.
decomposition. modularity. re-useibility.) block(s) of code make a function body.

* **Block of code** : a logical grouping of statements is called a block of code 
(iterative block, True/False block, fuction block etc.)

* Statement _DO_ something. Expression _REPRESENT VALUE_ of something.
* Central idea of coding - "D0 something based on some VALUE"

* **Statements** keyword(s) and expression(s) together form a statement. Example :
control-flow statement - if-statement, for & while statment, return statement etc.
defination statement - function defination, class defination etc.
These statement use keywords and the value(s) of certain expression(s).

* **Expressions** data objects and/or bindings together with operators in syntactically 
and semantically valid ways form expressions. Expressions can be/are evaluated to 
some value. Expressions can also involve "custom datatypes" and "custom operators". 

* **variables-value binding** : give names to data objects (a level in abstraction)
more general term for 'variable' is 'identifier'. used for any name given to different 
parts of a program (class name, function name, var name etc.)

* **Custom operators** implemented by defining `methods` (`functions` inside a `class`)
(a level of abstraction) 
* **Default operators** arithematic, comparision, logical, assignment. These operators 
can be overloaded to do different things by redefining them within the class.
example : 
```def __add__(self, other): # redefines what a + b would be```

* **Custom datatype** implemented by defining a `class` (a prototype for a `data object`)
* **Default datatype** are default data Objects of python . They can be classified as 
scalar vs non-scalar, mutable vs immutable, sequential vs mapping.
**data-structure** or compound data objects. Example - list, tuple, set dictionary, objects
**non-scalar** : can be broken into simpler types. example - string, list, tuple, set dictionary, objects
**scalar**     : cannot be broken into simpler types. example -  int, float, bool, NoneType 

Basic Algorithms
================

**Algorithm** is a systematic way to find a solution to a problem. Closely related terms are
**pseudo-code** and **flow-chart** to express this "systematic way" in plain english and in a
diagrammatic way respectively.

* **Guess and check** is an "exhaustive enumeration" method used when we have finite things to 
check/ eg. Prime or not).

* **Approximation** define an error range and take small steps to find soln. similar to guess 
and check method.

* **Bisection Search** used when we know the finite range within which the solution lies.
guess, check if big or small, repeat in smaller range. Bisection search used for monotonically 
increasing functions).

* **Newton-Raphson** approximation algorithm to find roots of polynomial in one variable.

Decomposition, Abstraction with Functions
=========================================

* **Decompose** the problem into smaller pieces, that is, Breakup a large problem into 
smaller problems.  
* **Abstraction** that is, supress details. Only input and output matter.
* **Functions** help achieve Abstraction and Decomposition.

* Fuctions let us group computations together and store them so that we can **call/invoke**
these functions later whenever needed (multiple times if needed)

* just like we use variable name to refer to a memory location, we can use the function 
name to refer to memory location where the function is saved.

* **Function specification/doc-string** tells us about the kinds of input the function is 
expecting and the kinds of output this function will give. (a comment)

* SYNTAX
```python
def funtion_name(parameter_1, parameter_2,...):
    """
    brief defination of what the function is doing.
    
    :param parameter_1: what does this parameter represents.
    :param parameter_2: what does this parameter represents.
    :return : what does the function return.
    """
    ...statements...
    return <value>
```
function name, parameters, docstring, body, return statement.
function name + parameters are called function signature
* **docstring** "contract". mention "Assumptions" and "Guarantee" result 
* **actual parameter** and **formal parameters**
actual parameter are the one used one funtion is being called.
formal parameter are the one used in the new frame created by the call.
* **frame and scope of variables** refer to the call by value and 
call by reference section.
* **Higher order programming** function with parameter as another function.
* **Helper function** are functions defined inside another function.
* **Decorators** use the concept of higher order programming and helper functions

Recursion vs Iteration
======================

* **Recursion** based on "divide-and-conquer" philosophy.
* Break larger problem into SIMILAR smaller problem.
* functions used the idea of break larger problem into smaller problems
* but if smaller problem is similar. **Call a function within itself**
* **Call Stack** stack of frames/scope with first-in-first-out property
* **Base case** most important. Helps terminate the call stack (stack = FIFO).
* Mathmatical induction used to prove statement for all (positive )integers
* Recursion and Mathematical Induction closely related.
* Classical problems : factorial, tower of hanoi, fibonacci.
* hanoi = multiple recursion calls in one frame
* fibonacci = multiple base cases (for 0 and 1)

Compound Datatype Tuple and Lists
=================================

* Tuple and List Example
```python
tup = (3, 'chirag')  # tup is a tuple 
lst = ['Brown', 31]  # lst is a list
```
* List and Tuple are based on the mathematical concept of **sequences**
* Tuple can be used for swapping `(x, y) = (y, x)`
* **Tuple Unpacking** is used to spend data to a called 
function in a more compact and secure way. (secure since
tupes are not mutable like lists)
* Tuple can be used to return multiple things `return (q,r)`
* Lists are like tuples but mutable
* Extensively use to group data together.

Higher Order programming
========================

* A funtion is also an object in python (has memory location)
* Function is itself treated as a primitive. Passed as parameter.
* One such function is the map(callable, iterable)

Compound Datatype Dictionary
============================

* Dictionary example
```python
 dt = {'Math1' : 'B', 'Math2' : 'A', 'EVS' : 'Good'}
```
* Generalization of a list. Based on mathematical notion of **mapping**
* A list is like a sequence and a dictionary is like a map.
* Just like a sequence is a 'special' map
* A list can be thought of as a special dictonary. 
* Map between 'key-value' pairs. Referencing dt['Math1'] # 'B'
* add entry, remove entry, test if key is present ('Math3' in dt # False)
* Important fuctions associated dt.keys(), dt.values(), dt.items()
* Key need to be immutable (int, float, string, tuple, bool)
* More strongly, Key needs to be hashable
* Dictionary used in **memoization** used during a recursive call
  to avoid multiple redundent computation (fibonnaci example)
* global variable (not recommened) breaks normal scoping rule
  used to show increase in efficiency by memoization

Debugging and Testing Code
==========================

Analogy :
> "making soup and bugs keep falling in from the ceiling"
* Cheak soup for bugs (**TESTING**/compare inputs and outputs)
* Keep lid closed (**DEFENSIVE PROGRAMMING**)
* Clean Kitchen (ELIMINATE SOURCE OF BUG - **DEBUGGING**)

Defensive Programming: 
----------------------
(a) write *docstring* and *comments*,
(b) *modularize* program, 
(c) check conditions on *input/output* (**ASSERTIONS**)

Testing
-------
Compare inputs and outputs make sure to write docstring
and make clear the assumptions you have made.
(a) Unit Testing : validate each piece of the program. 
    Test each function seperatedly.
(b) Regression testing : (unit) test again after fixing a bug 
(c) Integration testing : test overall program (after unit testing)
* use intuition regarding natural BOUNDARY of the problem 
random testing sample and checking outcomes

* Types of Testing Suite :
    * **BLACK BOX testing** : Don't look at code. just the docstring 
    (BOUNDARY and EXTREME inputs)
    * **GLASS BOX testing** : Look inside code. every potential path tested
    (BRANCHES, LOOPS within code)

Black Box Testing and Glass Box Testing in a Black Box Testing Suite 
we add all extreme cases of inputs to a function
in a Glass Box Testing Suite we add all possible paths within a function
(all if-elif-else, a loop runs 0,1 and multiple times.) 

* Types of Bugs in code :

    Based on how they show up :
    (a) Overt Bugs  : obvious manifestation - code crashes or runs forever
    (b) Covert Bugs : no obvioius manifestation - code returns a value which
    is incorrect but hard to determine
    
    Based on when they appear : 
    (a) Persistant   : occur everytime code is run (easy to detect)
    (b) Intermittent : occur sometimes (even with same input). Depend on other factors
    (dealing with the internet or with time etc.)

Defensive programming can help force bugs into the "overt persistant" class
of bugs which are easy to detect and correct.

Debugging
---------

* Read error message as it gives info about the type of error and the 
exact line of code where the error occured (and the call stack).
* Use "print" statements to narrow down on the location of the bug
* print when you enter a function defination. print the inputs. print before returning.
print half-way. Put print statements in other obvious places.
* IndexError, TypeError, NameError, SyntaxError.
* Logic Errors (Semantic Error) harder. Explain code (rubber duck method)
* Don't write entire code at once. Write module then test/debug. Write another 
module then test/debug it. then test the two modules together (unit testing,
regression testing and finally integration testing)


Exception and Assertions 
========================

Exception
---------

* Exceptions deal with the question :
>"What happens when a procedure execution hits an "unexpected" condition?"

* Possible "unexpected condition" : IndexError, TypeError, NameError, SyntaxError,
AttributeError, ValueError, IOError.
* In "regular code", Python will terminate code and display one of the above errortype
and a message giving details about the error (and the call stack that lead to that error).
* The possible things that we can do when a program encounters an error
    (a) Fail silently (BAD IDEA!)
    (b) return an "error" value 
    (c) stop execution. raise an error. 
Python raises some expections by default, **however we can manually raise exceptions as well**
* Pyhton code provides for error handlers for exceptions by the 
  **"try-except-else-finally" blocks**.        

Assertions 
----------

* Using the keyword **'assert'** we can ensure that a certain condition is met
before we carry forward with code excution. If this condition is not met, an AssertionError
is raised by python and the code does not execute further (we can however write the 'assert'
within a try-block and write an except block for AssertionError)
* Assertions are usually used for inputs to a function and before returning output 
 
Object Oriented Programming
===========================

* *Everything in Python is an object. Primitive datatype, functions etc. are all objects.*
Eg. grades = \[A, B, C, D, F\]. 'grades' is an object of the class 'list' with attributes 
(linked list nodes) and methods 'append()', 'pop()' etc.
* Every object has 3 things 
    (a) Type (or class)
    (b) Internal Representation 
    (c) Set of Procedures/Interface

* Creating **'custom datatypes'** and associated **'custom operators'**
* Custom datatype = 'internal representation' = 'data attributes' = 'data abstraction'
* Custom operator = 'set of procedures' = 'procedural attributes'/'methods' = 'encapsulating procedures'
* 'Object' wraps these two ideas (abstraction and encapsulation) together.
* Each object belongs to a 'class' or 'type' where these attributes and methods are 
defined. Object is an instance of a class.

* We can create a class by using **'class' keyword**
* We can create an object by calling the class as a function which
inturn calls the **__init__() method** defined inside the class 
* We refer to the attributes of any instance using the **'.' operator**
* We refer to the calling object using the **'self' keyword**
Example :
```pyhton
class Phone(object):
    def __init__(self, screen, ram, memory):
        self.screen = screen
        self.ram = ram
        self.memory = memory
        self.is_on = False
        
    def toggle_on_off(self)
        if self.is_on == False
            print("Powering on your smart-phone")
            self.is_on = True
        else
            print("Powering off your smart-phone")
            self.is_on = False
```

* WHY do OOP? 
bundle data into packages (logical organization of data) and 
divide-and-conquer development (class help with code modularity)

Creating an Object
==================
* When we call the class, the __init__() method creates a new instance
```python
oneplus = Phone(6.28, 6, 64)
```
* first parameter of 'init' (self) refers to an instance of the class
* other parameter is the initial data that the object is going to 'glue' together
* gluing done by creating bindings with the instance 'self'. (self.x = x)
* once binding is complete we have **instance variables** that are initialized with 
the provided values within that instance of the class (simply, object)

Assessing Object Attributes
===========================
Data Attributes
---------------
* we can access these instance variables of an object using the dot operator
```python
print(f"oneplus 6 screen size is {oneplus.screen}-inches")
```
* Think of object pointing to a frame (just like function calls creates a frame)
* Within this scope/frame we bind values to data attibutes (instance variables)
* To access these data attributes we say 
'goto frame `oneplus` and pick `screen` value in that' 
which when translating to code becomes `oneplus.screen`

Procedural Attributes
---------------------
* to access method of a class there are 2 ways : 
    (a) Use an instance to get to the method (self automatically refers to the
    calling object) c.distance(origin)
    (b) Use class to get to the method : provide all arguments manually. 
    Coordinate.distance(c, origin)

* object is a frame. class is a frame. object does not have method defined
inside. but since it is an instance of the class it **INHERITS** methods from
the class 
* isinstance(object, class) checkes if given object is instance of the given class

Getter and setter functions
===========================

* getter and setter function should be used to access and change object vaules 
rather than direct referencing. use "obj.getX()" rather than "obj.x"
use "obj.setX(5)" rather than "obj.x = 5"
* Bad practice to directly manipulate internal representation of an object
* We should seperate use of the object from what is inside

Inheritance subclasses and superclasses
=======================================

* Inheritance helps us reuse previous code (written for the superclass
object) while adding additional attribute (data as well as procedural)
to the subclass.
* While subclass can inherit attributes from the parent class, we can 
always  override the parent class methods by redefining the same 
method in the subclass
* Inheritance furthers the idea of code modularity since making changes
to the superclass automatically infulences the subclass. But not vice
versa. Therefore the Hierarchy should be made carefully
* **Substitution Principle** to improve the Hierarchy. 
* We can create a class with objects of other classes as its attributes

Generators
==========
* Generators allow us to generate as we go along, instead of holding everything in  memory.

* Generator functions allow us to write a function that can send back a 
value and then later resume to pick up where it left off.

* Generator functions will automatically suspend and resume their execution 
and state around the last point of value generation. This feature is known as state suspension.

* The keyword 'yield' makes all this possible. Other important functions
  are 'next()' and 'iter()'

* 'yield' - suspends execution, next() - resumes execution

Computational Complexity (algorithm vs algorithm in terms of speed and memory)
==============================================================================

* **"Readability"** = names/identifiers should be discriptive
* **"Modularity"** = Functions, Classes and Inheritance
* **"Scalability"** = Complexity of algorithm. Tradeoff between time and space

* Focus on Time Complexity. "How program 'scales' when input size grows?"
* Many ways to implement (recursive vs iterative) but only few algorithms
* Possible ways to compute (time) efficiency of algorithm:

(a) Time in milliseconds : varies with implementation, vaires between computers, not 
predictable base on small inputs. 

(b) Count Operations : assumes primitive operations (+, >, =) take constant time
now counting operations effectively is counting time. Varies with implementaion!
no idea which operation to count. Depend on input (which we want)

(c) Order of Growth : Decide input and how to measure its 'size'. BEST, WORST, AVERAGE. 
Worst- case most important. How the efficieny changes based on the size of input. 
Eg how will efficiency change if input doubles.
 
* For this we identify the slowest parts of the program and put an upper bound on the 
time and then this helps us classify the algorithm in different orders of growth.
constant, linear, quadratic, logarithmic, n log n, exponentail.
