lst1=[("Amit",),"sarika","namita",("Hardik",),"Natasha"]
boys= sum(1 for name in lst1 if isinstance(name, tuple))
girls = sum(1 for name in lst1 if isinstance(name, str))
print("Number of boys:",{boys})
print("Number of girls:", {girls})
