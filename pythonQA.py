def q1():
    print('Hello' * 5)


# this is swapping of variables in python
def q2():
    x, y = 4, 5
    y, x = x, y
    print(x)
    print(y)


def q3():
    z = 9
    lst = [0] * z
    print(lst[:-1])


def q4():
    def hel(x):
        return x % 2 == 0
    lst = [i ** 2 for i in range(10)]  # [0, 1, 4, 9, 16, 25, 36, 49, 81] then remove numbers not divisible by 2
    lst = filter(hel, lst)  # [0, 4, 16, 36, 64] filtered numbers divisible by 2
    print(list(lst)[::2])  # [0, 16, 64] skip the numbers by 2


def q5():
    z = 0
    for i in range(1, 10):
        if(i + 1 // 2) % 7 == 0:
            break
        else:
            z += int(i % 2 == 0)
    else:
        print('End')


def q6():
    import math
    for i in range(1, 10):
        if math.sqrt(i) == (1 - 5) ** 2:
            print(i)
            break
    else:
        print('No!')


def q7():
    class A:
        def __init__(self, x):
            self.x = x

        def __eq__(self, o):
            return self.x == o.x
    a = A(2)
    b = A(2)
    print(a == b)
    print(a is b)
    print(b is a)
    print(a is a)
    print(a == a)


def q8():
    class A:
        def __init__(self, x, y):
            self.x = x
            self.y = y

        def printer(self):
            print(self.x, self.y)

    class B(A):
        def printer(self):
            print(self.y, self.x)

    class C(B):
        def __init__(self, x, y, z):
            super().__init__(x, y)
            self.z = z

    d = A(2, 4)
    e = B(4, 5)
    g = C(3, 4, 7)
    g.x = g.z
    d.printer()
    e.printer()
    g.printer()


def q9():
    def x(z):
        def q(x, y):
            x = y + z + x
            print(x)
        return q
    for i in range(10):
        func = x(i)
        func(i, i-1)


def q10():
    def d(f):
        def w(*args, **kwargs):
            r = f(*args, **kwargs)
            r += 1
            return r
        return w

    @d  # decorator
    def a(x):
        return x + 1
    print(a(5))


def q11():
    print(*list(map(lambda x: chr(ord(x) + 1), ['a', 'b', 'c'])))


def q12():
    x = 0.1
    y = 0.1000000000001
    print(x == y)


def q13():
    x = [True, 1, "a", "b", "2"]
    print(any(x))


def q14():
    x = ["a", 1, 2, 3, 4]
    y = z = x
    z[1] = 7
    y[3] = 5
    x[2] = 9
    print(x)
    print(y)
    print(z)


def q15():
    print(1 == True)
    print("1" == 1)


def q16():
    x = b'1001'
    y = b'1010'
    z = x + y
    print(z)


def q17():
    x = 0b1001
    y = 0b1010
    z = x + y
    print(z)
