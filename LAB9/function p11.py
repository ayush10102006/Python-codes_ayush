def create_list(list1, list2):
    intersection = list(set(list1) & set(list2))
    return intersection
a = [10,20,30,40,50]
b = [40,50,60,70,80]
result = create_list(a, b)
print("Intersection:", result)
