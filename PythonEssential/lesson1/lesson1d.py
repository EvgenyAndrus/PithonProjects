class MyObj:
    class_attribute = 8

    def __init__(self):
        self.data_attribute = 42

    def instance_method(self):
        print(self.data_attribute)

    @staticmethod
    def static_method():
        print(MyObj.class_attribute)


if __name__ == '__main__':
    MyObj.static_method()
    obj = MyObj()
    obj.instance_method()
    obj.static_method()
