str = input("Enter a string: ")
char_frequency = {}
for char in str:
    if char in char_frequency:
        char_frequency[char] += 1
    else:
        char_frequency[char] = 1
print("Character Frequency:", char_frequency)
