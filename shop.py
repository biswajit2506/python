pname=["Apple","Banana"]
price={101:220,102:50}
disc={101:10,102:2}
class wrongproductid(Exception):
   pass
def cal():
  pid=int(input("Enter the Product id - "))
  if pid>103 or pid<101:
    raise wrongproductid;
  quan=int(input("Enter the Quantity - "))  
  cprice=price[pid]*quan
  print("Calculated price - ",cprice)
  discprice=cprice/100*disc[pid]
  print("Total Discount - ",discprice)
  finalprice=cprice-discprice
  print("Price After Discount - ", finalprice)
n='Y'
while n!='N':
  try:
    con=input("Do you want to Buy any item : ")
    if con.upper()=='Y':
      cal()
    else:
      print("Thank You for Visit")
      n='N'
  except wrongproductid:
    print("Please enter the correct id.")
