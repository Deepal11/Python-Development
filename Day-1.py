#Print statement
'''
print("Hello Deepal")
'''

#variable
'''
a=11
print("{} belongs to {}:".format(a,type(a)))
a="Deepal"
print("{} belongs to {}:".format(a,type(a)))
a=1.25
print("{} belongs to {}:".format(a,type(a)))
print(165648)
'''


#Taking input from user
'''
a=input("Enter string:")
print("Input is a string type",a)
a=int(input("Enter integer:"))
print("Input is of Integer type",a)
a=float(input("Enter float value:"))
print("Input is of Float type",a)
'''

#Dictionary
'''
d={1:1,2:8,3:27}
print("Printing dictionary:",d)
print("Printing keys of dictionary:",d.keys())
print("Printing values of dictionary:",d.values())
print("Printing items of dictionary:",d.items())
'''

#list
'''
a=[12,85,56,16,36,56]
print("List components:",a)
a.append(25)
print("Appending in list :",a)
a.insert(3,11)
print("Inserting a number at position 3:",a)
a.remove(36)
print("Deleting a specific number from list:",a)
del a[3]
print("Deleting a element from a specific index:",a)
a.pop()
print("Removing last element from a list:",a)
b=a.count(56)
print("Counting a specific element in list: ",b)
b=a.index(16)
print("Finding index of a element from list:",b)
a[0]=99
print("changing the element on 0th index with 99:",a)
a.sort()
print("Printing a sorted list:",a)
a.sort(reverse=True)
print("printing descending sorted list:",a)
print("Max of list:",max(a))
print("Min of list:",min(a))
print("sum of list:",sum(a))
print("Average of list:",sum(a)/len(a))
'''

#slicing in list
'''
print("Printing first 3 elements of list:",a[0:3])
print("accessing last element of list:",a[-1:])
print("accessing last 4 element of list:",a[-4:])
'''

#indexing
'''
print('Element at index 2:',a[2])
'''


#tuple
'''
tu=(1,2,4,5,7,8,9,6,4)
print("Printing tuple:",tu)
b=tu.count(4)
print("Counting number of occurrence of an element in tuple:",b)
b=tu.index(5)
print("Finding index of a element from tuple:",b)
'''

#Set
'''
s={1,12,1,3,2,5,16,7,8,9}
print("printing element of set:",s)
s.pop()
print("Removing element from set:",s)
s.add(456)
print("Adding element in a set:",s)
d={8,9,11,12,33}
print("Printing interrsection of 2 sets:",s&d)
print("Printing Union of 2 sets:",s|d)
'''


#If-Else
'''
a=11
if a%2==0:
    print("{} is even number.".format(a))
else:
    print("{} is odd number.".format(a))
'''

#For
'''
a=[1,2,3,4,5,6,7,8,9,10]
for i in a:
    print(i)
'''

#PATTERN
'''
#*
#**
#***
#****
for i in range(1,int(input("Enter limit: "))+1):
    print("*"*i)
'''

'''
#   *
#  * *
# * * *
#* * * *
n=int(input('Enter limit: '))
for i in range(1,n+1):
    print(" "*(n-i),end="")
    print("* "*i)
'''

#while
'''
i=1
while (i<11):
    print("I value is :{}".format(i))
    i+=1

#Pattern(Through while loop)
i=1
while(i<11):
    print("*"*i)
    i+=1
'''

#For Else
'''
for i in [2,5,7,3,6]:
    if i==8:
        print("found")
        break
        
else:
    print("not found")
'''

'''
aa=65    
print(chr(aa))
'''
'''
a='A'
print(ord(a))
'''

#Function definition
'''
def hello():
    print('Hello')
hello()
'''

'''
def add(a,b):
    print('Sum is:',a+b)
add(5,6)
'''
