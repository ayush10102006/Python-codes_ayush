import random
no=random.sample(range(15,45),10)
s1=set(no)
print(s1)
count=0
for ele in no:
    if ele<30:
        count=count+1
print(count,"numbers are below 30")
lst=list(s1)
for ele in lst:
    if ele>35:
        lst.remove(ele)
s1=set(lst)
print(s1)
        

    
