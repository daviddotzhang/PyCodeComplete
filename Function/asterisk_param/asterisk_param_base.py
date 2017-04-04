# coding=utf-8
"""
最初，星号变量是用在函数的参数传递上的，
在下面的实例中，单个星号代表这个位置接收任意多个非关键字参数，在函数的*b位置上将其转化成元组，
而双星号代表这个位置接收任意多个关键字参数，在**b位置上将其转化成字典
"""
# --------


def one(a, *b):
    """a是一个普通传入参数，*b是一个非关键字星号参数"""
    print(b)


one(1, 2, 3, 4, 5, 6)


# --------


def two(a=1, **b):
    """a是一个普通关键字参数，**b是一个关键字双星号参数"""
    print(b)


two(a=1, b=2, c=3, d=4, e=5, f=6)

"""
#程序输出
(2, 3, 4, 5, 6)
{'b': 2, 'c': 3, 'e': 5, 'f': 6, 'd': 4}
#从输出中可以看到，第一个函数中，*b的位置可以传入任意多没有关键字的参数，*b会将这些传入参数转化成一个元组，下面的调用
one(1,2,3,4,5,6)
#传入one(a,*b)后，等价与
one(1,(2,3,4,5,6))

#第二个函数中，**b的位置可以接收任意多个关键字参数，下面的调用
two(a=1,b=2,c=3,d=4,e=5,f=6)
#传入one(a,*b)后，等价与
two(a=1,{'b': 2, 'c': 3, 'e': 5, 'f': 6, 'd': 4})
"""