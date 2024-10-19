import module
import modul2 as mm #alias of module
from modeul3 import display #single function import from an module
from modeul3 import substraction as sub # function name change 
from mod4 import*
import platform



module.greeting("Abdul Azeeem")
module.add(6,8)
module.mul(4,5)

mm.mul(2,3)

# core modules 
x=platform.system()
print(x)
y=platform.machine()
print(y)
a=platform.architecture()
print(a)
b=platform.processor()
print(b)

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
display('good morning ')
sub(6,2)
