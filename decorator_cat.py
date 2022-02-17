'''Задача 1 1.1 Написать декоратор, который
перед запуском произвольной функции с произвольным набором аргументов
будет показывать в консоли сообщение "Покупайте наших котиков!" и возвращать
результат запущенной функции. 1.2 Параметризовать декоратор таким образом, чтобы сообщение,
печатаемое перед выполнением функции можно было задавать как параметр во время декорирования.'''
from random import randint
def deco_second_level(parameter):
    def deco_first_level(func):
        def wrapper(*args, **kwargs):
            print(parameter)
            func(*args, **kwargs)
            return func(*args, **kwargs)
        return wrapper
    return deco_first_level

@deco_second_level(parameter='Покупайте наших котиков')
def arbitrary_func():
    rand_int=randint(1,2)
    if rand_int==1:
        cat='Сиамская кошка'
    else:
        cat='Мейн-кун'
    return cat

print(arbitrary_func())


