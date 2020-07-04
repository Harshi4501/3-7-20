#(3)program to sum all the items in a list
l1=[]
n=int(input("enter total no of elements:"))
for i in range(n):
    x=int(input("enter the number:"))
    l1.append(x)
print(l1)
print("sum of all elements in the list is:",sum(l1))

