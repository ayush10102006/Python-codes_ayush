def ispalindrome(text):
    cleaned = text.replace(" ", "").lower()
    return cleaned == cleaned[::-1]
test1 = "Racecar"
test2 = "hello"
test3 = "thala for a reason"
print(f"'{test1}' is palindrome:", ispalindrome(test1))
print(f"'{test2}' is palindrome:", ispalindrome(test2))
print(f"'{test3}' is palindrome:", ispalindrome(test3))
