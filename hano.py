def hano(n, a, b, c):
    '''
    :param n: 代表几个盘子
    :param a: 代表A塔
    :param b: 代表B塔
    :param c: 代表C塔
    :return:
    '''
    if n == 1:
        print(a, "-->", c)
        return None
    # n == 2 可以不写，但是更容易理解
    if n == 2:
        print(a, "-->", b)
        print(a, "-->", c)
        print(b, "-->", c)
        return None
    # 先借助C塔，把n-1个盘子挪到B上，此时A塔上只有一个盘子，B塔上有n-1个盘子，C塔没有
    hano(n - 1, a, c, b)
    print(a, "-->", c)
    hano(n - 1, b, a, c)


a = "A"
b = "B"
c = "C"

n = 4

hano(n, a, b, c)
