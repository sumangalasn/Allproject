factorial=1
num=9
if num<0:
    print("the factorial number does not exit in negative number")
elif num==0:
    print("the factorial of 0 is 1")

else:
  for i in range(1,num+1):
      factorial=factorial*i
      print("the factoial of",num ,"is",factorial)
