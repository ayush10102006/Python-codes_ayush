num = int(input("Enter a number: "))
if num < 2:
    prime = False
else:
    prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            prime = False
            break

sum_factors = 0
for i in range(1, num):
    if num % i == 0:
        sum_factors += i
perfect = sum_factors == num
num_str = str(num)
num_length = len(num_str)
armstrong_sum = sum(int(digit) ** num_length for digit in num_str)
armstrong = armstrong_sum == num
palindrome = num_str == num_str[::-1]
square = num ** 2
automorphic = str(square).endswith(str(num))
print(f"Prime: {'Yes' if prime else 'No'}")
print(f"Perfect: {'Yes' if perfect else 'No'}")
print(f"Armstrong: {'Yes' if armstrong else 'No'}")
print(f"Palindrome: {'Yes' if palindrome else 'No'}")
print(f"Automorphic: {'Yes' if automorphic else 'No'}")
