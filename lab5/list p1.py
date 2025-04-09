import random
odd=random.sample(range(1, 100, 2), 5)  
even=random.sample(range(2, 100, 2), 4)
print("Odd numbers:", odd)
print("Even numbers:", even)
odd[2] = even
flattened_sorted_list = sorted(sum(([x] if isinstance(x, int) else x for x in odd), []))
print("Final sorted list:", flattened_sorted_list)
