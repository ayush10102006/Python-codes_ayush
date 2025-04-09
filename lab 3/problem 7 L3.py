#npr
n=int(input("Enter a number:"))
r=int(input("Enter a number:"))
fact=1
for i in range(1,n+1):
    fact=fact*i
num=fact
factorial=1
for j in range(1,(n-r)+1):
    factorial=factorial*j
den=factorial
npr=num/den
print(npr)
#ncr
factr=1
for k in range(1,r+1):
    factr=factr*i
ncr=num/(den*factr)
print(ncr)

