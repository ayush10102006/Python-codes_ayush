l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
l2 = [2, 4, 6, 8]
l3 = [num for num in l1 if num not in l2]
print("List 1:", l1)
print("List 2:", l2)
print("List 3 (Elements from List 1 not in List 2):", l3)

