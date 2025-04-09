import random
lst=random.sample(range(1,100),20)
print("list:",lst)
n=int(input("Enter a number:"))
for ele in lst:
    if n==ele:
        print(lst.index(n))
