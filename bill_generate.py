pname=["Apple","Toor Dal","Sugar","Onion"]
price={101:220,102:110,103:55,104:45}
disc={101:10,102:0,103:5,104:5}
pid={101:"Apple",102:"Toor Dal",103:"Sugar",104:"Onion"}
class worngproductcode(Exception):
  pass
def cal():
  id=int(input("Enter Product ID - "))
  if id not in pid:
    #print("Incorrect Product Code.")
    raise worngproductcode
  else:
    quan=float(input("Quantity in Kg- "))
    iprice=price[id]*quan
    print("Initial Price -",iprice)
    dprice=int(iprice/100*disc[id])
    print("Discount -",dprice)
    fprice= iprice-dprice
    print("Final Price -",fprice)
    return pid[id],quan,iprice,dprice,fprice

n='Y'
allitems=[]
while n!='N':
  try:
    con=input("Do you want to Buy anything - ")
    if con.upper()=='Y':
      a,b,c,d,e=cal()      
      allitems.append(a)
      allitems.append(b)
      allitems.append(c)
      allitems.append(d)
      allitems.append(e)
    else:
      #print("Thank You Visit Again.")
      n='N'
  except worngproductcode:
    print("Incorrect Product Code.")
#print(allitems)
pn=0
pquan=1
pprice=2
pdprice=3
pfprice=4
total=0
total_dis=0
total_price=0
l=int(len(allitems)/5);
print("Product         Quantity    Price   Discount   Final Amt")
print("--------------------------------------------------------")
for i in range(0,l):
  print(allitems[pn].ljust(14," "),"    ",str(allitems[pquan]).ljust(3," "),"   ",str(allitems[pprice]).ljust(5," "),"   ",str(allitems[pdprice]).ljust(6," "),"    ",allitems[pfprice])
  total_price=total_price+allitems[pprice]
  total_dis=total_dis+allitems[pdprice]
  total=total+allitems[pfprice]
  
  pn=pn+5
  pquan=pquan+5
  pprice=pprice+5
  pdprice=pdprice+5
  pfprice=pfprice+5
  print("--------------------------------------------------------")
print("Total Bill  \t\t\t   ",total_price,"     ",total_dis,"\t\t ",total)
print("---------------- Thank You Visit Again -----------------")
