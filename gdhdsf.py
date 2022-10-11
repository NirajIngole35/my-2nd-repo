import numpy
from numpy import ones, zeros
x=array.array('i',[1,2,3,4,5,6])
print(x) 
print(type(x)) 

#second way 
from array import*
x=array('i',[1,2,3,4,5,6]) 
print(x) 
print(type(x))
list=[34,4,5,6,7,8,8]
sum = 0
for i in  range(len(list)):
    sum = sum + list[i]
print(sum)
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")



#multiply no.using while loop
h=float(input("enter yr no."))
i=1
while i<=10:
     print(i*h)
     i=i+1
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
#multiply no.using for loop
h=float(input("enter yr no."))
for i in range(1,11):
     print(i*h)
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
#PASS OR FAIL USING IF,ELSE
h=float(input("enter yr MARK IN 100:"))
if h>=35:
     print("pass")
else: 
     print("dfbg")
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")

#squre of no.
h=float(input("enter yr no."))
print(h**2)
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")

#area of circle
h=float(input("enter yr R."))
print("r of circle:- ",3.14*h**2)

print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")

#add nature no.using while 
h=int(input("enter yr no."))
sum=0
i=1
while i<=h:
     
     sum=sum+i
     i=i+1
print(sum)
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")