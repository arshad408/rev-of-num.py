num=int(input("Enter the nuumber:"))
rev=0
while(num>0):
  rem=num%10
  rev=(rev*10)+rem
  num=num//10
print("Reverse of num is =",%rev)
