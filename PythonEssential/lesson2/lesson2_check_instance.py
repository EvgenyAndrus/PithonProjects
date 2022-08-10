#  примеры. логика работы
#  isinstance(obj, cls)
def check_instance(obj, cls):  # obj является экземпляром класс cls
    # return cls in type(obj).mro()
    return check_subclass(type(obj), cls)


#  issubclass(cls, base)
def check_subclass(child, base):  # child является подклассом класса base
    # return base in child.mro()
    if child == base:
        return True
    for direct_base in child.__bases__:
        if base == direct_base:
            return True
        return check_subclass(direct_base, base)
    return False

