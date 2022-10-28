def my_fct(*args, **kwargs):
    print("{} - {}".format(args, kwargs))

my_fct() # () - {}
my_fct("Best") # ('Best',) - {}
my_fct("Best", 89) # ('Best', 89) - {}
my_fct(name="Best") # () - {'name': 'Best'}
my_fct(name="Best", number=89) # () - {'name': 'Best', 'number': 89}
my_fct("School", 12, 8, name="Best", number=89, b="c") # ('School', 12) - {'name': 'Best', 'number': 89}

print("--------")

def my_fct(*args, **kwargs):
    print("{} - {}".format(args, kwargs))

a_dict = { 'name': "Best", 'age': 89 }

my_fct(a_dict) # ({'age': 89, 'name': 'Best'},) - {}
my_fct(*a_dict) # ('age', 'name') - {}
my_fct(**a_dict) # () - {'age': 89, 'name': 'Best'}

print("New__" * 10)

class Foo(object):
    def __init__(self, a_value1, a_value2, a_stack=None, *args, **kwargs):
        """do something with the values"""
        super(Foo, self).__init__(*args, **kwargs) # to objects constructor fwiw, but object.__init__() takes no args
        self.value1 = a_value1
        self.value2 = a_value2
        self.stack = a_stack
        return

    def __str__(self):
        return ', '.join(['%s: %s' % (k, v) for k, v in self.__dict__.items()])


class MyFoo(Foo):
    def __init__(self, not_for_Foo, *args, **kwargs):
        # do something else, don't care about the args
        super(MyFoo, self).__init__(*args, **kwargs)
        self.not_for_Foo = not_for_Foo # peals off
        self.myvalue1 = 'my_' + self.a_value1 # already set by super


if __name__ == '__main__':

    print('Foo with args')
    foo = Foo('Python', 2.7, 'my stack')
    print(foo)

    print('\nMyFoo with kwargs')
    myfoo = MyFoo('my not for foo', value2=2.7, value1='Python', stack='my other stack')
    print(myfoo)



