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
