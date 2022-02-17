'''Задача 4 4.1
Написать декоратор, который бы измерял время работы функции и
печатал бы его на экран. 4.2
Доработать декоратор
таким образом, чтобы в логах было название запускаемой функции помимо времени
исполнения.
4.3 Доработать декоратор так, чтобы запись
лога для функции велась в файл, путь к
которому нужно было бы задавать во время декорирования, как параметр.'''


import time
def deco_second_level(parameter):
    def deco_first_level(func):
        def wrapper(*args, **kwargs):
            start=time.time()
            res=func(*args, **kwargs)
            stop=time.time()
            at='time: %f\nname of function: %s' % ((stop-start),func.__name__)
            print(at)
            f=open(parameter, 'w')
            f.write(at)
            f.close()
            return res
        return wrapper
    return deco_first_level


@deco_second_level(parameter='d:/factorial_time.txt')
def somefunc(): #this function consider factorial 50000
    factorial = 1
    for i in range(1, 50000):
        factorial *= i
    return  factorial

print(somefunc())

