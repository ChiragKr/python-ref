(SCALAR) data objects - int, float, bool, NoneType (primitives)
putting primitives together using operators (expression)
using expressions' outcome to dictate logic (statements) 
logically grouping multiple statements together (block)
expression constructed in valid ways (syntax)    |syntax error 
expression make sense (semantic/static semantic) |logical error
assign names to object (abstraction)
variable name and value bindings ('=' use to bind name to value)
first evaulate right side expression then bind to name on left side
make assignment ("=" assignment operators)
doing calculations (arithematic operators)
making decisions   (boolean operators + logical operators)
logical operators to combine boolean expression (compound boolean)

===================================================================

if-else construct : TEST/True-block/False-block
elif : series of tests performed in the order it is typed 

===================================================================


(NON-SCALAR) string - sequence of (case-sensitive) characters. (primitive)
"+" string concatination ("+" is being overloaded here)
type of oparand tells operator what to do.
"*" multiple concatination ("*" is overloaded)
we can compare string (lexicographically)
len(<string>) : returns number of characters
<string>[index] : return element at index "index" | IndexError
<string>[start_index:end_index:step]

===================================================================

input/output
print to monitor using "print" keyword print(<object>, <object>, ...)
input(<object>) ==> console input as a string | input into environment

===================================================================

while-loop --syntax : (look out for : variable, condition, update)
for-loop --syntax : (look out for : variable)
break - terminates loops execution
"variable" = "looping variable"
decrimenting function.

===================================================================

branching and looping blocks...
guess-and-check methods [guess uses loop; check uses "if"]
guess-and-check = "exhaustive enumeration"
approximate solution

===================================================================

Distribution = set of python packages/modules pre-installed with python
environment = user selected packages/modules included
conda/pip = package manager used to download/include packages into an environment.
python shell = where code is written/recieved and interpreted in an environment

package : modules together form a package. can to imported to other piece of code.
.py files : form a module. can to imported to other piece of code
.py file = expressions(s)/code that is stored that when run is sent to the shell

code = lots of expressions/"blocks of code"/functions make code

functions : (encapsulation. abstraction. decomposition. modularity. re-useibility)
			block(s) of code make a function body.

block of code : statements make a block of code (iterative block and/or decision 					block, fuction block etc.)

[Statements DO something. Expressions REPRESENT value.]
[D0 something based on some VALUE]

statements  : control-flow (if-statement/for & while statment/return) uses keywords
			  and the value(s) of certain expression(s).
expressions : putting primitives/variables together using operators in syntactically 			   and semantically valid ways. [expressions are evaluated]
			  expressions can also involve "custom operators" aka functions/methods 


"custom operator" : aka functions (a level of abstraction)
operators = arithematic, comparision, logical, assignment, (operator overloading)

variables/binding : give names to primitives (a level in abstraction)
[more general term for 'variable' is 'identifier'...used for any name given to different parts of a program (class name, function name, var name etc.)]

"data-structure"/compound data objects : list, tuple, set dictionary, objects
non-scalar : string, list, tuple, set dictionary, objects
scalar     : int, float, bool, NoneType, 
Data Objects : scalar vs non-scalar, mutable vs immutable
			   sequential vs mapping.

===================================================================

Algorithms :-
> Guess and check (when we have finite things to check/ eg. Prime or not)
> Approximation (define error range. take smaller steps to find soln.)
> Bisection Search (range, guess, guess big or small, repeat in smaller range)
  (Bisection search used for monotonically increasing functions)
> Newton-Raphson (approx algo. to find roots of polynomial in one variable)

===================================================================

Decomposition, Abstraction with Functions :-
> Break up large problem into smaller problems
> Supress details. only input and output matter
> Abstraction and Decomposition achieved by functions
> fuctions let us group computations together
> function specification/doc-string
> function name, parameters, docstring, body
> docstring = "contract"; mention "Assumptions" and "Guarantee" result 
> actual parameter and formal parameters
> frame and scope of variables
> function with parameter as another function
> function (called helper function) inside another function.

====================================================================

Recursion vs Iteration
> Recursion based on "divide-and-conquer" philosophy.
> Break larger problem into SIMILAR smaller problem.
> functions used the idea of break larger problem into smaller problems
> but if smaller problem is similar. Call a function within itself!
> Base case most important. Helps terminate the call stack (stack = FIFO).
> "call stack" = stack of frames/scope with first-in-first-out property
> Mathmatical induction used to prove statement for all (positive )integers
> Recursion and Mathematical Induction closely related.
> Classical problems : factorial, tower of hanoi, fibonacci.
> hanoi = multiple recursion calls in one frame
> fibonacci = multiple base cases (for 0 and 1)

====================================================================

Tuple tup = (3, 'chirag') and Lists lst = ['Brown', 31]
> Tuple can be used for swapping (x, y) = (y, x)
> Tuple can be used to return multiple things return (q,r)
> Lists are like tuples but mutable
> Expensively use to group data together.

====================================================================

Higher Order programming
> A funtion is also an object in python (has memory location)
> Function is itself treated as a primitive. Passed as parameter.
> One such function is the map(callable, iterable)

====================================================================

Dictionary dt = {'Math1' : 'B', 'Math2' : 'A', 'EVS' : 'Good'}
> Generalization of a list. Based on mathematical notion of mapping
> A list is like a sequence and a dictionary is like a map.
> Just like a sequence is a 'special' map
> A list can be thought of as a special dictonary. 
> Map between 'key-value' pairs. Referencing dt['Math1'] # 'B'
> add entry, remove entry, test if key is present ('Math3' in dt # False)
> Important fuctions associated dt.keys(), dt.values(), dt.items()
> Key need to be immutable (int, float, string, tuple, bool)
> More strongly, Key needs to be hashable
> Dictionary used in memoization used during a recursive call
  to avoid multiple redundent computation (fibonnaci example)

> global variable (not recommened) breaks normal scoping rule
  used to show increase in efficiency by memoization

====================================================================

Debugging and Testing Code
> Analogy.."making soup and bugs keep falling in from the ceiling"
> Cheak soup for bugs (TESTING/compare inputs and outputs)
> Keep lid closed (DEFENSIVE PROGRAMMING)
> Clean Kitchen (ELIMINATE SOURCE OF BUG - DEBUGGING)
--------------------------------------------------------------------

Defensive Programming: 
(a) write docstring and comments ,
(b) modularize program, 
(c) check conditions on input/output (ASSERTIONS)

--------------------------------------------------------------------

Testing : compare inputs and outputs make sure to write docstring
and make clear the assumptions you have made.
(a) Unit Testing : validate each piece of the program. 
    Test each function seperatedly.
(b) Regression testing : (unit) test again after fixing a bug 
(c) Integration testing : test overall program (after unit testing)
> use intuition regarding natural BOUNDARY of the problem 
> random testing sample and checking outcomes
> BLACK BOX testing : Don't look at code. just the docstring 
(BOUNDARY and EXTREME inputs)
> GLASS BOX testing : Look inside code. every potential path tested
(BRANCHES, LOOPS within code)

--------------------------------------------------------------------

Exception and Assertions

====================================================================

Object Oriented Programming
> Everything in Python is an object. Primitive datatype, functions etc.
  are all objects.
> Eg. grades = [A, B, C, D, F]. 'grades' is an object of class 'list' with
  attributes (linked list nodes) and methods 'append()', 'pop()' etc.
> Every object has 3 things 
(a) Type (b) Internal Representation (c) Set of Procedures/Interface

> Creating 'custom datatypes' and associated 'custom operators'
> Custom datatype = 'internal representation' = 'data attributes' = 'data abstraction'
  Custom operator = 'set of procedures' = 'procedural attributes'/'methods' = 'encapsulating procedures'
> 'object' wraps these two ideas (abstraction and encapsulation) together.
> each object belongs to a 'class' or 'type' where these attributes and methods are
  defined. object is an instance of a class.
> CREATING a class (using 'class' keyword) and 
  CREATING an object (using classname and __init__() method)and 
  USING this instance (using the '.' operator and 'self' keyword)
> WHY do OOP? 
bundle data into packages (logical organization of data) and 
divide-and-conquer development (class help with code modularity)

====================================================================

Creating an object
> when we call the class, the __init__() method creates a new instance 
> first parameter of 'init' (self) refers to an instance of the class
other parameter is the initial data that the object is going to 'glue' together
> gluing done by creating bindings with the instance 'self'. (self.x = x)
> once binding is complete we have 'instance variables' are initialized with the 
provided values within that instance of the class (simply, object)
> we can access these instance variables of an object using the dot operator
> Think of object pointing to a frame (just like function calls creates a frame)
> Within this scope/frame we bind values to data attibutes (instance variables)
> to access these we say 'goto frame c and pick x value in that frame' = c.x
> to access method of a class there are 2 ways : 
(a) Use an instance to get to the method (self automatically refers to the
    calling object) c.distance(origin)
(b) Use class to get to the method : provide all arguments manually. 
    Coordinate.distance(c, origin)

> object is a frame. class is a frame. object does not have method defined
  inside. but since it is an instance of the class it INHERITS methods from
  the class 

> isinstance(object, class) checkes if given object is instance of the given class