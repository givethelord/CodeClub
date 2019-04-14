#!/usr/bin/env python


def print_1(func):
    def general_decorator(*args, **kwargs):
        print("print_1")  # 装饰器附加功能
        ret = func(*args, **kwargs)  # 函数本来功能执行
        return ret  # 函数本来功能执行返回结果
    return general_decorator


def print_content(text):
    def print_style(func):
        def common_decorator(*args, **kwargs):
            print(text)  # 装饰器附加功能
            ret = func(*args, **kwargs)  # 函数本来功能执行
            return ret  # 函数本来功能执行返回结果
        return common_decorator  # 函数本来功能执行返回结果
    return print_style


class Docorator(object):
    def __init__(self, fuc):
        self.fuc = fuc

    def __call__(self, *args, **kwargs):
        print("decorator start")
        self.fuc(*args, **kwargs)
        print("docorator stop")

    @classmethod
    def print_2(cls, func):
        def general_decorator(*args, **kwargs):
            print("print_2")  # 装饰器附加功能
            ret = func(*args, **kwargs)  # 函数本来功能执行
            return ret  # 函数本来功能执行返回结果
        return general_decorator

    @staticmethod
    def print_3(text):
        def print_style(func):
            def common_decorator(*args, **kwargs):
                print(text)  # 装饰器附加功能
                ret = func(*args, **kwargs)  # 函数本来功能执行
                return ret  # 函数本来功能执行返回结果

            return common_decorator  # 函数本来功能执行返回结果

        return print_style


class Docorator_1(object):
    def __init__(self, dec):
        print("__init__")
        print(dec)

    def __call__(self, func):
        print("__call__")

        def waaa(*args, **kwargs):
            return func(*args, **kwargs)
        return waaa


@print_content('print_content')
@print_1
@Docorator
@Docorator.print_2
@Docorator.print_3("print_3")
@Docorator_1("ssasa")
def prin_dd(dd):
    print(dd)


print("test")
prin_dd(22)
