l1=[("Pizza",100),("Burger",90),("Cookies",80)]
sorted_items = sorted(l1, key=lambda item: item[1], reverse=True)
print(sorted_items)
