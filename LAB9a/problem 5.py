faculty_names = ['Dr. Sharma', 'Prof. Mehta', 'Dr. Anuradha Singh', 'Prof. Arvind', 'Ms. Priya', 'Dr. Kaushik']
long_names = list(filter(lambda name: len(name) > 8, faculty_names))
print("Faculty names with more than 8 characters:")
for name in long_names:
    print(name)
