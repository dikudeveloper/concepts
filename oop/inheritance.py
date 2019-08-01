
class A:
    def func(self):
        return 'A.func()'


class B(A):
    def func(self):
        return 'B.func()'


class C(B, A):
    pass


if __name__ == '__main__':
    a = A()
    b = B()
    c = C()

    # print(a.func())
    print(c.func())