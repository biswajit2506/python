list=[10,20,30,10,20,40,50,60,70,10,10,20,20]
s=set(list)
print(s)
for i in s:
  count=list.count(i);
  print(i,"count of ",count)
