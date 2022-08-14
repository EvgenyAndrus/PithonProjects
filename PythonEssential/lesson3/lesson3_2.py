class MyObject:
    def __del__(self):  # деструктор
        print('destructor invoked')
        raise Exception
#        print(self, 'is about to be deleted')


print('creating object')
o = MyObject()
print('deleting reference')
del o
print('done')
