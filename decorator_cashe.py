'''Задача 3 3.1
Написать кэширующий декоратор. Суть в том, что если декорируемая
функция будет запущена с теми параметрами с которыми она уже запускалась - брать
результат из кэша и не производить повторное выполнение функции.
3.2 Сделать так, чтобы
информация в кэше была актуальной не более 10 секунд. Предусмотреть механизм
автоматической очистки кэша в процессе выполнения функций.
3.3 Параметризовать время кэширования в декораторе.'''
import datetime
def cash(func):
    _cash={}
    def wrapped(*args, **kwargs):
        nonlocal _cash
        if not _cash.get(args):
            res=func(*args, **kwargs)
            _cash[args]=res
            return func(*args, **kwargs)
        else:
            return _cash[args]
    return wrapped

@cash
def factorial(n):
    factorial = 1
    for i in range(1, n):
        factorial *= i
    return factorial


print(factorial(10))



