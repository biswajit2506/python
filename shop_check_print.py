def search(s):
  list=["apple","orange","kiwi"]
  avl=[]
  navl=[]
  nval=0;
  s=s.split(",")
  #print(s)
  #print(type(s))
  for j in s:
    nval=0;
    for i in list:     
      if j==i:
        #print(j," Avaiable in our Shop.")
        avl.append(j)
        break;
      else:
        nval=nval+1;
    #print(nval)
    if nval==len(list):
      navl.append(j)
      #print(j," Is not avaiable in our Shop.")
  avl.insert(0,"Avaiavle List")
  navl.insert(0,"Not Avaiavle List")#print(avl)
  #print(navl)
  return avl,navl
s=input("Enter the Fruits U Want to Search - ")
#print(search(s))
x,y=search(s)
print("---------",x[0],"--------")
for i in x:
  if i!='Avaiavle List':
   print(i)
print("---------",y[0],"--------")
for j in y:
  if j!='Not Avaiavle List':
    print(j)
