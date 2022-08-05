class MyObject:
    def __init__(self):
        self.password = None

    def __getattribute__(self, item):
        if item == 'secret_field' and self.password == 'qqq':
            return 'Secret Value'
        else:
            return object.__getattribute__(self, item)
