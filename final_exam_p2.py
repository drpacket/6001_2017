class A(object):
    def foo(self):
        print('hi')
class B(A):
    def foo(self):
        print('bye')

a = A()

b = B()

print(isinstance(a, A))

print(issubclass(b, A))




