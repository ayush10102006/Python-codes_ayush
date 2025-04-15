def generate_tuples(end):
    result = []
    for x in range(1, end + 1):
        result.append((x, x**2, x**3))
    return result
ending_value = 5
tuples_list = generate_tuples(ending_value)
print(tuples_list)
