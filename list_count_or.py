list=[10,20,30,10,20,50,70,90,80,30,30,10,10,80]
flag=False
while flag!=True:
  val=list[0]
  print(list)
  print(val)
  count=list.count(val)
  print(val," Number of times - ",count)
  for i in range(0,count):
    list.remove(val)
    if len(list)==0:
      flag=True
