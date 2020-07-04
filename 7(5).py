#(7)program to sum all the items in a dictionary
d={1:2,3:4,5:6}
sum1=0
sum2=0
for i in d:
    sum1=sum1+i
    sum2=sum2+d[i]
sum3=sum1+sum2
print("the sum of all items in the dictionary:",sum3)



