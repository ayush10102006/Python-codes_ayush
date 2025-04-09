import random
lst=[random.randint(-100, 100) for ele in range(30)]
positive=[]
negative=[]
for ele in lst:
    if ele>0:
        positive.append(lst)
    print(positive)
    if ele<0:
        negative.append(lst)
    print(negative)


