def search(s):
  list=['apple','banana','orange','kiwi']
  s=s.split(',')
  for i in s:
    val=0
    for j in list:
      if i==j:
        print(i,"is aailable in our shop")
        break
      else:
        val=val+1
    if val==len(list):
      print(i,"is not available in our shop")

enter=input("Enter fruit you want to buy:")
search(enter)
