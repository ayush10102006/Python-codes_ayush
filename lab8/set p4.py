s1={"Ayush","Bob","Aman","Brett","Amit","Brian"}
a_names = set()
b_names = set()
for name in s1:
    if name.startswith('A'):
        a_names.add(name)
    elif name.startswith('B'):
        b_names.add(name)
print("Names starting with 'A':", a_names)
print("Names starting with 'B':", b_names)
