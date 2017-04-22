import lab_work_5_2.definitions as defs

main_var = 'main module variable'

if __name__ == '__main__':
    defs.function_two(main_var)
else:
    print("Execution module {}".format(__name__))
