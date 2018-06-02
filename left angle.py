x=int(input("enter the no"))
y=2*x-2
for i in range(0,x):
    for j in range(0,y):
        print (end= " ")
    y = y-2
    for j in range(0,i+1):
         print("*",end=" ")
    print()
