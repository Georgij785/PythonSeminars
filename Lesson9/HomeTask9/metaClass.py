class Singlton(type):
    a = None

    def __call__(self, *args, **kwargs):
        if self.a == None:
            self.a = type.__call__(self, *args)
            # ...и добавим ему переданные в вызове аргументы в качестве атрибутов.
            for name in kwargs:
                setattr(a, name, kwargs[name])
                # вернем готовый объект
        return self.a


class MyClass(metaclass=Singlton):
    pass


a = MyClass()
b = MyClass()

print(a is b)
