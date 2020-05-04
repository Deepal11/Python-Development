#function with no return
def add(a,b):
    c=a+b
    print('Sum of {} and {}: {}'.format(a,b,c))

#function with return value
def sub(a,b):
    c=a-b
    return 'Difference of {} and {}: {}'.format(a,b,c)

#function with multiple return values
def cal(a,b):
    c=a+b
    d=a-b
    return c,d

#DEFAULT arguments
def person(name,gender='Female'):
    print('Person name is',name,'and gender is',gender)

#KEYWORD arguments
def info(name,age):
    print('Person name is',name,'and is',age,'years old.')

#VARIABLE-LENGTH arguments
def func(*args):
    s=0
    for i in args:
        s+=i
    print('Sum of given',len(args),'numbers is:',s)

#inner function
def outer(name):
    n=name
    def inner():
        print(n)
    inner()

def main():
    #no return value
    add(5,6)

    #single return value
    s=sub(6,5)
    print(s)

    #multiple return values
    a,s=cal(12,5)
    print(a,s)

    #calling function with DEFAULT argument
    person('Deepal')

    #calling function with KEYWORD arguments
    info(age=22,name='Deepal')

    #calling function with VARIABLE-LENGTH arguments
    func(5)
    func(5,6)
    func(2,4,6,5,8)

    #inner function
    outer('Deepal')

if __name__=="__main__":
    main()
