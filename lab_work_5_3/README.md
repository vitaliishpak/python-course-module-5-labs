##Laboratory Work 5.3

####Description:

Create two modules were import from each other present that placed in different folders

####Here is its solution code:

**main_pack**
*main.py*
```python
import sys
import lab_work_5_3
import lab_work_5_3.defs
import lab_work_5_3.defs.definition as defs
from lab_work_5_3.defs.definition import*

import lab_work_5_3 as defs

main_var = 'main module variable'

if __name__ == '__main__':
    defs.function_two(main_var)
else:
    print('Execution module{path}'.format(path=__file__))
```

**defs**
*definitions.py*
```python
import lab_work_5_3
import lab_work_5_3.main_pack
import lab_work_5_3.main_pack.main
from lab_work_5_3.main_pack.main import*


def function_one():
    print('Function one call!')


def function_two(variable):
    print("function two call: {path}!".format(path=variable))


pi = 3,14

if __name__ == '__main__':
    print('definitions module executed!')
    print('PI = ', pi)
    function_one()
```

**defs**
*main_window.py*
```python
import lab_work_5_3
import lab_work_5_3.main_pack
import lab_work_5_3.main_pack.main
from lab_work_5_3.main_pack.main import*

import lab_work_5_3
import lab_work_5_3.defs
import lab_work_5_3.defs.definition as defs
from lab_work_5_3.defs.definition import*

if __name__ == '__main__':
    defs.function_two(main_var)
else:
    print('Execution module{path}'.format(path=__file__))
```