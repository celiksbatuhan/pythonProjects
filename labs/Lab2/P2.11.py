x=float(input("Enter a value of x: "))
y=float(input("Enter a value for y: "))
if x>0 and y>0:
    print("1")
elif x<0 and y>0:
    print("2")
elif x<0 and y<0:
    print("3")
elif x>0 and y<0:
    print("4")
elif x==0 and y==0:
    print("0")
else:
    print("on the x or y axis")