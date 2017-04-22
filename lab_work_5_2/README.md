##Laboratory Work 5.2

####Description:

Create two modules were import from each other present

####Here is its solution code:

*main.py*
```python
import lab_work_5_2.definitions as defs

main_var = 'main module variable'

if __name__ == '__main__':
    defs.function_two(main_var)
else:
    print("Execution module {}".format(__name__))
```

*definitions.py*
```python
from lab_work_5_2.main import *


def function_one():
    print('function one call!')


def function_two(variable: str):
    print("function one call: '%s'!" % variable)


pi = 3.14

if __name__ == '__main__':
    print('definitions module executed!')
    print('PI = ', pi)
    function_one()
```