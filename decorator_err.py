'''Задача 2 2.1 Написать декоратор, который внутри себя выполнял бы функцию и возвращал
бы результат её работы в случае успешного выполнения. В случае возникновения ошибки во
время выполнения функции нужно сделать так, чтобы выполнение функции было повторено ещё
раз с теми же самыми аргументами, но не более 10 раз. Если после последней попытки функцию
так и не удастся выполнить успешно, то бросать исключение.
2.2 Параметризовать декоратор таким образом,
чтобы количество попыток выполнения функции можно было задавать как параметр во время декорирования.'''

def deco_second_level(*dargs, **dkwargs):
    def deco_first_level(func):
        def wrapper(*args, **kwargs):
            attemptions=dkwargs['attemptions']
            while attemptions>0:
                try:
                    return func(*args, **kwargs)
                except Exception as err:
                    res='Error-->%s\nattemtions left-->%d' % (err, attemptions)
                    print(res)
                    attemptions-=1
        return wrapper
    return deco_first_level
@deco_second_level(attemptions=10)
def division(a, b):
    return a/b

print(division(5,0))