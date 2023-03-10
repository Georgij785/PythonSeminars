# класс для дескриптора 1
class Simple_Validate():
    def __get__(self, instance, owner):
        return instance.__dict__[self.attr]

    def __set__(self, instance, value):
        try:
            if value == 1 or value == 2:
                instance.__dict__[self.attr] = value;
            else:
                for i in range(2, value):
                    if (value % i == 0) & (value != i):
                        raise Exception()
                instance.__dict__[self.attr] = value;
        except Exception:
            print("Число не простое")

    def __delete__(self, instance):
        del instance.__dict__[self.attr]

    def __set_name__(self, owner, name):
        self.attr = name


class Simple_numbers():
    # дескриптор 1
    number = Simple_Validate()

    def __init__(self, value):
        self.number = value


# класс для дескриптора 2
class more_than_5():
    def __get__(self, instance, owner):
        return instance.__dict__[self.attr]

    def __set__(self, instance, a):
        try:

            if a < 5:
                raise Exception()
            instance.__dict__[self.attr] = a;
        except Exception as err:
            print("Число меньше 5-ти")

    def __delete__(self, instance):
        del instance.__dict__[self.attr]

    def __set_name__(self, owner, name):
        self.attr = name


class number_more_5():
    number = more_than_5()

    def __init__(self, value):
        self.number = value


n = Simple_numbers(2)

n.number = 4

print(n.number)

a = number_more_5(56)
a.number = 3

print(a.number)




