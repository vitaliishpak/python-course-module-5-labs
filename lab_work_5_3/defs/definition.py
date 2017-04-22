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
