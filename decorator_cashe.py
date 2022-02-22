'''Задача 3 3.1
Написать кэширующий декоратор. Суть в том, что если декорируемая
функция будет запущена с теми параметрами с которыми она уже запускалась - брать
результат из кэша и не производить повторное выполнение функции.
3.2 Сделать так, чтобы
информация в кэше была актуальной не более 10 секунд. Предусмотреть механизм
автоматической очистки кэша в процессе выполнения функций.
3.3 Параметризовать время кэширования в декораторе.'''
import time
def cash(func):
    _cash={}
    _time=time.time()
    def wrapped(*args, **kwargs):
        nonlocal _cash
        if args[0] not in _cash.keys():
            res=func(*args, **kwargs)
            _cash[args[0]]=res
            print('from func')
            return func(*args, **kwargs)
        else:
            print('from cash')
            return _cash[args[0]]
    return wrapped

@cash
def factorial(n):
    factorial = 1
    for i in range(1, n):
        factorial *= i
    return factorial


print(factorial(10))
print(factorial(10))
print(factorial(11))




