class Base:
    def method(self):
        print('Hello')


class Child(Base):
    def child_method(self):
        print('Hello from child method')

    def method(self):
        print('hello from redefine method')


o = Child()
o.method()
o.child_method()
