from abc import ABC, abstractmethod

#abstract class
class A(ABC):
    @abstractmethod
    def demo(self):
        print('Abstract base class')

class B(A):
    def demo(self):
        super().demo()
        print('Child class\n')

if __name__=="__main__":
    # cannot instantiate abstract parent class
    #a=A()

    #object of child class
    b=B()
    b.demo()

    #dividing by zero generates error and terminated program
    #a=10/0
    
    #EXCEPTION HANDLING
    #to avoid termination: try-except
    try:
        n=int(input('Enter divisor: '))
        a=10//n
        print(a)
    except:
        print('Zero division error')

    #multiple exceptions
    try:
        n=int(input('Enter divisor: '))
        a=10//n
        print(a)
    except ZeroDivisionError:
        print('Zero division error')
    except ValueError:
        print('invalid literal of int() with base 10')
    except:
        print('Invalid input')

    #try-else-finally
    try:
        n=int(input('Enter divisor: '))
        a=10//n
    except:
        print('Zero division error')
    else:           #exucutes only if there is no exception
        print(a)
    finally:        #always executes
        print('OVER\n')

    #FILE HANDLING
    #write mode
    f1=input('Enter file name: ')+'.txt'
    fh1=open(f1,'w')
    fh1.write('My name is Deepal Jain.\n')
    fh1.close()
    print('Successfully written\n')

    #append mode
    fh1=open(f1,'a')
    fh1.write('I live in Jaipur.')
    fh1.close()
    print('Successfully appended\n')

    #read mode using with open
    try:
        with open(f1,'r') as w:
            print(w.read())
    except Exception as e:
        print(e)
    else:
        print('\nSuccessfully read\n')
