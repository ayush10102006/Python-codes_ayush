t=((1,2,3),(),(4,5,6))
lst=list(t)
del lst[1]
t=tuple(lst)
print(t)
