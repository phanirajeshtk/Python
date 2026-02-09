#For Loop ################################################
x = ['navin',65,2.5]
for i in x:
    print(i)

for i in range(11,20,1):
    print(i)

for i in range(1,21):
  if(i%5!=0):
    print(i)

#print all the perfect sqaure number between 1 and 500

for i in range(1,501,1):
    sqrnumber = i * i
    if(sqrnumber < 500):
        print(sqrnumber)

################## Break Continue Pass#####################
availablecandies = 10
x =int(input("How many candies do you want"))
i=1
while i<=x:
    if(i>availablecandies):
        print("Not enough candies")
        break

    print("candy")
    i=i+1

print("Bye")


for i in range(1,101):
    if i % 2!=0:
       pass
    else:
     print(i)


#1) Print first 50 fionacci numbers 2) check a given number is prime or not

#1,1,2,3,5,8,13,21
import math
i=0
j=1
count=1
while count<=50:
    fibvalue = i+j
    i=j
    j=fibvalue
    if count <= 50:
        print(fibvalue)
        count+=1


#check a given number is prime or not
x = int(input("enter a number to check if the given number is prime or not"))
if x % 2 != 0:
    print(x,"is a prime number")
else:
    print(x,"is a even number")

#patterns
for i in range(4):
    for j in range(4):
        print("#",end="")
    print()

for i in range(4):
    for j in range(i+1):
        print("#",end="")


for i in range(4):
    for j in range(i, 4):
        print(j + 1, end="")
    print()

#Array
from array import *
vals = array('i',[5,9,8,4])
print(vals)
print(vals.buffer_info())
print(vals.append(10))
vals.reverse()
print(vals)
for i in range(len(vals)):
    print(vals[i])
for e in vals:
    print(e)

#Array New Array copying
from array import *
vals = array('i',[1,2,3,4,5,6,7,8,9])
newArray = array(vals.typecode, (a for a in vals))
print(newArray)

# Write a code to sort the array in ascending order
from array import *
vals = array('i',[1,2,3,4,5,6,31,98,-1])
sorterarray= sorted(vals)
print(sorterarray)

# Write a code to find factorial of a given number
import math as m
from math import factorial

vals = int(input("enter the number for which you need factorial"))
print(factorial(vals))

# write a code to ask the user to enter the array lengh and data to be entered and for which data user wants to perform search
from array import *
arr = array('i',[])
n = int(input("enter the lengh of the array"))
for i in range(n):
    x=int(input("enter the element"))
    arr.append(x)

print(arr)

val = int(input("enter the value to be searched"))
k=0
for e in arr:
    if e == val:
       print(k)
       break

    k=k+1

print(arr.index(val))

## Deleting value from Index#2 without using inbuilt functions
from array import *
arr = array('i',[1,2,3,4,5])
index = 2
for i in range(index,len(arr)):
   arr[i] = arr[i] + 1
arr = arr[:-1]
print(arr)

#Numpy
from numpy import *
arr = array([1,2,3,4,5],int)
print(arr)

# Ways of creating an array
#aray()
#linspace()
#logspace
#arrange()
#zeros()
#ones()

from numpy import *

arr = array([1,2,3,4,5,6.0],float)
print(arr)
print(arr.dtype)

#linspace()
from numpy import *

arr = linspace(0,16,17)
print(arr)
#print(arr.dtype)

#arrange()
from numpy import *

arr = arange(0,10,2)
print(arr)
#print(arr.dtype)


# Copying an array
#vectorized operation
from numpy import *
arr1 = array([1,2,3,4,5,6,7,8,9])
arr2 = array([6,8,9,10,15,16,17,18,19])
arr3 = arr1 + arr2
print(arr3)

# Copying an array
#vectorized operation
from numpy import *
arr1 = array([1,8,3,4,5])
arr2 = arr1.copy()
arr1[1] = 2
print(arr1)
print(arr2)
print(id(arr1))
print(id(arr2))

#Keywarded Variable Length
def person(name, **data):
    print(name)
    for i,j in data.items():
        print(i,j)

person('rajesh',age=39,City='mumbai',mobile='94827')

#Global Keyword

def something():
    a= 9
    print("in function something", a)
    x = globals()['a']
    print(id(x))
    print(a)
    globals()['a']=15
    print(globals()['a'])

a = 15
print("out functional ", a)
print(id(a))
something()

#Ask user to enter number of names to enter, and check the lengh of each name and count number of names with lenghth greater than 5
a = int(input("how many names you want to enter"))
lst=[]
for i in range(a):
    lst.append(input("enter name"))

def count_names():
    count=0
    for n in range(len(lst)):
        if len(lst[n])> 5:
            count=count+1
        else:
            continue


    print(count)
    print(lst)

count_names()


#lambda filter(), map(). reduce()
#lambda
from functools import reduce


nums = [1,2,3,4,5,23,7,8,9,10]
evens = list(filter(lambda n:n%2==0,nums))
doubles =list(map(lambda n:n*2,evens))
sum = reduce(lambda a,b:a+b,doubles)


print(sum)
print(evens)
print(doubles)



#decorators
def div(a,b):
    print(a/b)

def smart_div(func):
    if a<b:
        a,b = b,a
        return func(a,b)
    return inner
div = smart_div(div)
div(2.4)

#Constructor, Self, Objects
class Computer:
    def __init__(self):
        self.cpu = 'I5'
        self.memory = '16GB'
    def config(self,cpu,memory):
        self.cpu = cpu
        self.memory = memory
        print(self.cpu,self.memory)
    def update(self):
        self.cpu='i3'
        self.memory='8GB'
    def compare(self,other):
        if self.cpu == other.cpu:
            return print('they both are same')
        else:
            return print('they are different')

C1=Computer()
C2=Computer()
C1.config('i9','18GB')
C1.update()
print(C1.cpu,C1.memory)
C1.compare(C2)

####################Inheritance#################################
class A:
    def feature1(self):
        print("feature1")
    def feature2(self):
        print("feature2")

class B:
    def feature3(self):
        print("feature3")
    def feature4(self):
        print("feature4")

class C(A,B):
    def feature5(self):
        print("feature5")

C1=A()
C2=B()
C3=C()
###################################################################
############################Duck Typing#########################
class Pycham:
    def execute(self):
        print("SpellCheck")
        print("AutoComplete")

class myeditor:
    def execute(self):
        print("SpellCheck")
        print("AutoComplete")
        print("console")
        print("execute")
class Laptop:
    def code(self,ide):
        ide.execute()

ide=myeditor()
lap1 = Laptop()
lap1.code(ide)
#################################################################


##################################Operator Overloading#######################

class Student:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2
    def __add__(self,other):
        m1=self.m1+other.m1
        m2=self.m2+other.m2
        s3=Student(m1,m2)
        return s3
    def __sub__(self,other):
        m1=self.m1-other.m1
        m2=self.m2-other.m2
        s3=Student(m1,m2)
        return s3
    def __mul__(self,other):
        m1=self.m1*other.m1
        m2=self.m2*other.m2
        s3=Student(m1,m2)
        return s3
    def __gt__(self,other):
        r1=self.m1+other.m1
        r2=self.m2+other.m2
        if r1>r2:
            return True
        else:
            return False

s1=Student(10,20)
s2=Student(20,30)
s3=s1+s2
print("{} {}".format(s3.m1,s3.m2))

#####################################################################################

############################Method Overloading#####################################
class Student:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2
    def sum(self, a=None, b=None,c=None):
        s=0
        if a!=None and b!=None and c!=None:
            s=a+b+c
        elif a!=None and b!=None:
            s=a+b
        else:
            s=a

        return s
s1=Student(10,20,)

print(s1.sum(5,6,9))

#####################################################################################

###########################Method Overiding ######################################

class A:
    def show(self):
        print("A")

class B:
    def show(self):
        print("B")

a1=B()
a1.show()

###################################################################################

##############################Iterator############################################
class TopTen:
    def __init__(self):
        self.num = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.num <= 10:
            val = self.num
            self.num += 1
            return val
        else:
            raise StopIteration


Values = TopTen()
for num in Values:
    print(num)

##################################################################################
################### Exception Handling ##########################################

a =5
b =int(input("enter a number"))
try:
    print(a/b)
except ValueError as e:
    print(e)
except Exception as e:
    print(e)
except ZeroDivisionError as e:
    print(e)
finally:
    print("cloded")


####################################################################################
###############################Mutli Threading ################################################

from threading import *
from time import sleep
class myThread1(Thread):
    def run(self):
        for i in range(10):
            print("Thread 1")
            sleep(1)
class myThread2(Thread):
    def run(self):
        for i in range(10):
            print("Thread 2")
            sleep(1)
t1=myThread1()
t2=myThread2()
t1.start()
t2.start()
t1.join()
t2.join()
print("done")

###################################################################################################
#######################File Handling - Read#####################
f = open("MyData.txt","r")
print(f.readline(),end="")

###########################################################################

###########################File Handling- Write ##############################
f1 =open("Demo.txt","w")
f = open("MyData.txt","r")
for data in f:
    f1.write(data)




###########################################################################