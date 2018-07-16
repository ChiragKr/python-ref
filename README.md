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

block of code : statements make a block of code (iterative block and/or decision 
block, fuction block etc.)

[Statements DO something. Expressions REPRESENT value.]
[D0 something based on some VALUE]

statements  : control-flow (if-statement/for & while statment/return) uses keywords
and the value(s) of certain expression(s).
expressions : putting primitives/variables together using operators in syntactically
and semantically valid ways. [expressions are evaluated]
expressions can also involve "custom operators" aka functions/methods 


"custom operator" : aka functions (a level of abstraction)
operators = arithematic, comparision, logical, assignment, (operator overloading)

variables/binding : give names to primitives (a level in abstraction)
[more general term for 'variable' is 'identifier'...used for any name given to 
different parts of a program (class name, function name, var name etc.)]

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

Types of Testing Suite :

> Testing of 2 type: Black Box Testing and Glass Box Testing
in a Black Box Testing Suite we add all extreme cases of inputs to a function
in a Glass Box Testing Suite we add all possible paths within a function
(all if-elif-else, a loop runs 0,1 and multiple times.) 

-----------------------------------------------------------------

Types of Bugs in code :

> Bugs are of two type:
(a) Overt Bugs  : obvious manifestation - code crashes or runs forever
(b) Covert Bugs : no obvioius manifestation - code returns a value which
is incorrect but hard to determine

(a) Persistant   : occur everytime code is run (easy to detect)
(b) Intermittent : occur sometimes (even with same input). Depend on other factors
(dealing with the internet or with time etc.)

Defensive programming can help force bugs into the "overt persistant" class
of bugs which are easy to detect and correct.

--------------------------------------------------------------------

Debugging : 

> Read error message as it gives info about the type of error and the 
exact line of code where the error occured.
> Use "print" statements to narrow down on the location of the bug
> print when you enter a function defination. print the inputs. print before returning.
print half-way. Put print statements in other obvious places.
> IndexError, TypeError, NameError, SyntaxError.
> Logic Errors (Semantic Error) harder. Explain code (rubber duck method)
> Don't write entire code at once. Write module then test/debug. Write another 
module then test/debug it. then test the two modules together

====================================================================

Exception and Assertions :

Exception : 

> Exceptions deal with the question - "What happens when a procedure
execution hits an "unexpected" condition?"

> Possible "unexpected condition" : IndexError, TypeError, NameError, SyntaxError,
AttributeError, ValueError, IOError.

> In regular code, Python will terminate code and display one of the above errortype
and a message giving details about the error

> The possible things that we can do when a program encounters an error
(a) Fail silently (BAD IDEA!)
(b) return an "error" value 
(c) stop execution. raise an error. 
Python raises some expections by default, however we can manually raise exceptions as well
> Pyhton code provides for error handlers for exceptions by the 
  "try-except-else-finally" blocks.        

--------------------------------------------------------------------

Assertions : 
> Using the keyword 'assert' we can ensure that a certain condition is met
  before we carry forward with code excution. If this condition is not met, an AssertionError
  is raised by python and the code does not execute further (we can however write the 'assert'
  within a try-block and write an except block for AssertionError)
> Assertions are usually used for inputs to a function and before returning output 
 
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

> isinstance(object, class) checkes if given object is instance of the given

=======================================================================

> getter and setter function used to access and change object vaules 
rather than direct referencing. use "obj.getX()" rather than "obj.x"
use "obj.setX(5)" rather than "obj.x = 5"
> Bad practice to directly manipulate internal representation of an object
> We should seperate use of the object from what is inside

=======================================================================

Inheritance subclasses and superclasses
> Inheritance helps us reuse previous code (written for the superclass
  object) while adding additional attribute (data as well as procedural)
  to the subclass.

> While subclass can inherit attributes from the parent class, we can 
  always  override the parent class methods by redefining the same 
  method in the subclass

> Inheritance furthers the idea of code modularity since making changes
  to the superclass automatically infulences the subclass. But not vice
  versa. Therefore the Hierarchy should be made carefully

> Substitution Principle to improve the Hierarchy. 

> We can create a class with objects of other classes as its attributes

=======================================================================

Generators
> Generators allow us to generate as we go along, instead of holding 
  everything in  memory.

> Generator functions allow us to write a function that can send back a 
  value and then later resume to pick up where it left off.

> Generator functions will automatically suspend and resume their execution 
  and state around the last point of value generation. This feature is known as state suspension.

> The keyword 'yield' makes all this possible. Other important functions
  are 'next()' and 'iter()'

> 'yield' - suspends execution, next() - resumes execution

  =======================================================================

Computational Complexity (algorithm vs algorithm in terms of speed and memory)
> "Readability" = names/identifiers should be discriptive
> "Modularity" = Functions, Classes and Inheritance
> "Scalability" = Complexity of algorithm. Tradeoff between time and space
> Focus on Time Complexity. "How program 'scales' when input size grows?"
> Many ways to implement (recursive vs iterative) but only few algorithms
> Possible ways to compute (time) efficiency of algorithm:

(a) Time run-time : varies with implementation, vaires between computers, not 
predictable base on small inputs. 

(b) Count Operations : assumes primitive operations (+, >, =) take constant time
now counting operations effectively is counting time. Varies with implementaion!
no idea which operation to count. Depend on input (which we want)

(c) Order of Growth : Decide input and how to measure its 'size'. BEST, WORST, AVERAGE. 
Worst- case most important. How the efficieny changes based on the size of input. 
Eg how will efficiency change if input doubles.
 
> For this we identify the slowest parts of the program and put an upper bound on the 
time and then this helps us classify the algorithm in different orders of growth.
constant, linear, quadratic, logarithmic, n log n, exponentail

 =========================================================================