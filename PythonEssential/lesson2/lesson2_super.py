class Base:
    def method(self):
        print('base method invoked on', type(self).__name__, 'instance')


class Child(Base):
    def method(self):
        super().method()
#       super(Child, self).method()
        print('child method invoked on', type(self).__name__, 'instance')


base = Base()
# base.method()
child = Child()
child.method()
#  Base.method(child)
