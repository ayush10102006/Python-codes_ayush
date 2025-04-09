import random
l1 = [random.randint(1, 30) for _ in range(50)]
l2 = list(dict.fromkeys(l1))
print("Original List (with duplicates):", l1)
print("List After Removing Duplicates:", l2)

