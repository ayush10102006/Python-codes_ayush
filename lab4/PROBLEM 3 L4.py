str1=input("Enter first string:")
str2=input("Enter second string:")
if str1 in str2:
    print("str1 is present in str2")
elif str2 in str1:
    print("str2 is present in str1")
else:
    print("not present")
