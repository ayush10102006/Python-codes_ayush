x=int(input("Enter x coordinate:"))
y=int(input("Enter y coordinate:"))
r=int(input("Enter the radius:"))
h=int(input("Enter first point:"))
k=int(input('Enter second point:'))
if (pow(x-h,2)+pow(y-k,2)<pow(r,2)):
    print("It lies inside the circle")
elif(pow(x-h,2)+pow(y-k,2)>pow(r,2)):
    print("Point lies outside the circle")
elif(pow(x-h,2)+pow(y-k,2)==pow(r,2)):
    print("Point lies on the circle")


