#(10)program to create a tuple
l=[]
n=int(input("enter the number of elements to be created in a tuple:"))
for i in range(n):
    x=input("enter the element:")
    l.append(x)
t=tuple(l)
print(t)




