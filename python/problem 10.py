l=int(input("Enter length:"))
b=int(input("Enter breadth:"))
area=l*b
perimeter=2*(l+b)
print("The area is",area)
print("The perimeter is",perimeter)
if area>perimeter:
    print("Area is greater than perimeter")
else:
    print("Perimeter is greater than area")
