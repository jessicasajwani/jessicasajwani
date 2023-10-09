l=[]
n=int(input("enter no. of elements"))
for i in range(n):
    a=int(input("enter element:"))
    l[i]=a
for i in range(0,n,2):
    print(l[i]*2)