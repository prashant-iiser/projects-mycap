print("FIBONACCI SERIES")
x=0
y=1
z=int(input("enter how many numbers you want: "))
for i in range(0,z):
    l=x+y
    print(l)
    x=y
    y=l
