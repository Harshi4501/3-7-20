#(8,9)to concatenate dictionaries and to create a new one
d1={1:10, 2:20}
d2={3:30, 4:40}
d3={5:50,6:60}
d2.update(d3)
d1.update(d2)
print(d1)




