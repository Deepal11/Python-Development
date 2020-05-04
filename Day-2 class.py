#import library
import math

#class creation
class Example:
    #constructor
    def __init__(self):
        #self is to refer object
        print('Instance of class Example created')

#class with method
class Circle:
    #constructor to initialize variable
    def __init__(self,r):
        #local variable -> r
        #instance variable -> self.r
        self.r=r
        print('Radius of circle:',r)
    #method
    def area(self):
        area=math.pi*self.r*self.r
        print('Area of circle: {:.2f}'.format(area))

#single inheritance
class A:
    def __init__(self):
        print('Parent class constructor')
    def demo(self):
        print('Parent class method')
class B(A):
    def __init__(self):
        super().__init__()  #super() to call methods of parent class from child class
        print('Child class constructor')
    #function overriding
    def demo(self):
        print('Child class method')

#multiple inheritance
class C1:
    def __init__(self):
        print('First parent')
class C2:
    def __init__(self):
        print('Second parent')
class C3(C1,C2):
    def __init__(self):
        super().__init__()
        print('Child class inherited from two parents')

#multi-level inheritance
class D1:
    def __init__(self):
        print('Grandparent')
class D2(D1):
    def __init__(self):
        super().__init__()
        print('Parent')
class D3(D2):
    def __init__(self):
        super().__init__()
        print('Child')

#decorators, class method and static method
class E:
    company='Celebal Technologies'      #class variable
    def __init__(self,name):
        self.name=name
    @classmethod        #decorator
    def clsmethod(cls):
        print('Company name is',cls.company)
    @staticmethod
    def statmethod():
        print('Static method')

#inner class
class Employee:
    def __init__(self):
        self.name='Deepal'
        self.doj=self.DOJ()
    def display(self):
        print('Name:',self.name)

    class DOJ:
        def __init__(self):
            self.dd=1
            self.mm=5
            self.yy=2020
        def display(self):
            print('Date of joining: {}/{}/{}'.format(self.dd,self.mm,self.yy))

def main():
    #object of class Example
    Example()

    #object of class Circle
    c=Circle(5)
    #calling class method using dot (.) operator
    c.area()

    #single inheritance
    #creating object of child class
    b=B()
    #accessing parent class method
    b.demo()

    #multiple inheritance
    c=C3()

    #multi-level inheritance
    d=D3()

    #class and static methods
    e=E('Deepal')
    E.clsmethod()
    E.statmethod()

    #outer class object
    emp=Employee()
    emp.display()
    #inner class object
    empdoj=emp.DOJ()
    empdoj.display()

if __name__=="__main__":
    main()
