import math


#def fact(n):
 #return(math.factorial(n))


#num=int(input("enter the number:"))
#f=fact(num)
#print("factorial of",num,"is",f)

factorial=1
num=5
if num<0:
 print("the nagetive number does not give factorial num")
else:
 for i in range(1,num+1):
     factorial=factorial*i
print("the factorial of",num ,"is",factorial)
