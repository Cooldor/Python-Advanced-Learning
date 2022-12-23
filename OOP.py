# An object - any unit of information in memory
# Class is a kind of instruction by which data types are created from objects
# Instance - specific object of some class
# Method - a function in a class to act on an object
# Fields or properties - variables inside the class
# Attributes - all names inside the class (of variables and methods)

class Purse:                        # simple class that doing nothing
    pass                            # pass ia a 'null' operator that is doing nothing


x = Purse()
print(type(x))


class Purse:            # functions is a method of classes
    @staticmethod
    def show(name='Unknown user'):        # parameter (self) for passing the name of the variables
        print('Greetings' + name + '!')  # in which the class is launched


x = Purse()
y = Purse()
x.show()
y.show('Albus')
print(y)


class Purse:
    def __init__(self):         # (__init__) operator, the code inside this method executed when
        self.money = 0.00       # an instance of a class created
    # it is called object constructor
    # this is necessary so that when creating a class,
    # immediately pass some values to it (properties)

    def info(self):
        return self.money        # (self.) makes it an instance(object) property for (x or y, etc...)


x = Purse()
y = Purse()

x.money = 100         # after a dot can call a method or assign a value to a variables(properties) inside a class
print(y.info())
print(x.info())


class Purse:
    def __init__(self, currency, name='Unknown'):
        if currency not in ('USD', 'EUR'):
            raise ValueError
        self.__money = 0.00                         # __ or _ before a variable(property) - encapsulation
        self.currency = currency                    # encapsulation for limit variables call inside a class
        self.name = name                            # now it is private (protected)

                                                    # _ more loyal encapsulation than __
    def top_up_balance(self, how_many):             # it is possible to get access to the variable in this case
        self.__money = self.__money + how_many
        return how_many

    def top_down_balance(self, how_many):
        if self.__money - how_many < 0:
            print('Insufficient funds!')
            raise ValueError('Insufficient funds!')     # (raise) - instruction to force an exception (if needed)
        self.__money = self.__money - how_many
        return how_many

    def info(self):
        print(self.__money)  # positional parameter(self) makes it an instance(object) property for (x or y, etc...)

#    def __del__(self):       # object destructor opposite to object constructor
#        print('The purse deleted')   # will be executed while deleting an object
#        return self.__money


x = Purse('USD')
y = Purse('EUR', 'Jojo')
y.top_up_balance(200)
x.top_up_balance(100)
x.money = -200         # impossible to assign a value to a properties, because they are encapsulated (__)
# x.top_down_balance(200)  # will be error with forced exception
# del x
x.top_up_balance(y.top_up_balance(50))  # transferring funds from wallet to wallet (return statements needed
x.info()                                # in top up  and top down methods with how_many parameter)
y.info()

from Classes import Verification
# inheritance in classes
# in inheritance classes we can add new methods and redefine old ones from the 'mother' class


class V2(Verification):                 # importing another class form different .py file

    def __init__(self, login, password, age):
        Verification.__init__(self, login, password)  # no need to rewrite all source (old) code from 'mother' class
        self.save()         # so that do not need to write its launch forcibly under the class (112th string)
        self.age = age

    def save(self):                     # now it is overriding method in (Verification) class
        with open('users') as r:        # it will be executed firstly
            for i in r:                 # it is needed to add more functionality to the old method
                if (f'{self.login, self.password}' + '\n') == i:        # from 'mother' class (Verification)
                    raise ValueError('Such password/login already exists')
        Verification.save(self)
# calling a 'mother' class with an inherited method so no need to rewrite all its source (old) code

    def show(self):
        return self.login, self.password, self.age


# x = V2('Max', '12345678', 23)
# x.save()               # looking for class method (save) firstly in (V2) class, then in imported(Verification)
# print(x.show())

from tkinter import Tk, Button


class MyApp(Tk):

    def __init__(self):
        Tk.__init__(self)
        self.geometry('400x400')
        self.setui()

    def setui(self):
        Button(self, text='OK').pack()          # composition is when we call some other class in the 'main' class


root = MyApp()
root.mainloop()


class V3(Verification):

    def __init__(self, login, password, age):
        super().__init__(login, password)   # method (super) searches for methods in parent classes on its own
        self.age = age
        self.__save()                             # no need to write parameter (self) with (super) method

    def __save(self):
        with open('users') as r:
            for i in r:
                if (f'{self.login, self.password}' + '\n') == i:
                    raise ValueError('Such password/login already exists')
        super().save()

    def show(self):
        return self.login, self.password, self.age


x = V3('Overlor', '12345678', 24)
# x.save()
# print(x.show)


# multiple inheritance

class A:                        # super class (without inheritance)
    def a(self):
        print('A')


class B:                        # super class
    def a(self):
        print('B')


class C(B):                     # subclass with inheritance
    def a(self):                # polymorphism - same name of method in all classes but different functionality
        print('C')


class D(C, A):                  # subclass
    def a(self):                # (super) function searches up to the first matching method (a), so in class (c)
        super(B, self).a()             # linearize(linearization)
        print(self.__class__.__mro__)   # shows exactly how python will look for a method of inherited classes
# in parentheses of (super) method, parameters are written to clarify the place where the search starts


D().a()
print(D.__mro__)                # another way to call the algorithm (__mro__)
from datetime import datetime as dt


class Player:                   # class that will create instance of players in game
    __LVL, __HEALTH = 1, 100    # properties of class (Player)
    __slots__ = ['__lvl', '__health', '__born']
# for faster access to class attributes. It will not be possible to Add new properties,
# to the instance that are not listed here ( an exception will be thrown)

    def __init__(self):
        self.__lvl = Player.__LVL   # calling of property syntax
        self.__health = Player.__HEALTH
        self.__born = dt.now()

    @property                      # (property) - decorator
    def lvl(self):                 # getter method is needed in order to get the value
        return self.__lvl, f'{dt.now() - self.__born}'          # of the encapsulated property (lvl)

    @lvl.setter                    # setter for two methods with the same name
    def lvl(self, numeric):
        self.__lvl += Player.__typetest(numeric)
        if self.__lvl >= 100:
            self.lvl = 100

    @classmethod        # decorator that interacts not with instances(like previous) but with the class itself
    def set_cls_field(cls, lvl=1, health=100):  # (cls) parameter will get not the specific variable like (self),
        cls.__LVL = Player.__typetest(lvl)                         # but the name of executed class
        cls.__HEALTH = Player.__typetest(health)

    @staticmethod      # (static) - working like simple function, just belongs to the class namespace
    def __typetest(value):
        if isinstance(value, int):  # this function checks if a value in a variable belongs to some data type
            return value
        else:
            raise TypeError('Must be int')


Player.set_cls_field(50)
x = Player()            # first player
# print(x.get_lvl())
# print(x.set_lvl(2))
# print(print(x.get_lvl()))
print(x.lvl)    # different syntax for decorator (property) and setter usage
x.lvl = 5       # looks like method (lvl) masquerades as a variable so no need to call it with ()

Player.set_cls_field()
y = Player()     # second player
print(y.lvl)

# y.lvl = 2.3  # will be the raised error because 2.3 not int value
