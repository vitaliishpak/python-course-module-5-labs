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
