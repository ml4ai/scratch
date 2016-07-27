# Python Package / Module reference examples

Example of using \_\_init\_\_.py to allow for relative package/module 
path references 

root1.py contains a function hello() that sets off a chain of calls to 
other functions, in this order, demonstrating the ability of call from 
a function to other functions:
- root1.hello()
- dir1.d1f1.hello()
- dir2.d2f1.hello()
- dir1.dir1_1.d1_1f1.hello()
- dir2.d2f2.hello()

On the other hand, you can execute dir1.dir1_1.d1_1f2.py as a 
standalone and it will call: dir2.d2f2.hello()

NOTE: for dir1.dir1_1.d1_1f2.py to access dir2.d2f2, it must import 
that entire path: import dir2.d2f2 .
However, for dir1.dir1_1.d1_1f1.hello() to access dir2.d2f2, it only
needs to import dir2 ; I'm not quite sure why.