__author__ = 'chira'

'''
Modular coding capabilities of python. We can write
different parts of the code in different files and
can simple IMPORT them to current file and use it
in current file rather than writing the code again.
Closely related to the notion of code reusability.
'''

import Modules_import # a custom made python file
import random         # an in-built python file

# INCORRENT to write "module_function()" must specify file
Modules_import.module_function() # <file name>.<function name>()

x = random.randrange(1,1000)
print(x)


