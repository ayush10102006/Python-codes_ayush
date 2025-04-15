def create_array(a,b,c,value):
    array = [[[value for _ in range(c)] for _ in range(b)] for _ in range(a)]
    return array
array_3d = create_array(1,2,3,'n')
for i, layer in enumerate(array_3d):
    print(f"Layer {i}:")
    for row in layer:
        print(row)
    print()
