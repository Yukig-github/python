#3FS1-75 福田湧基
#week4-2課題 if,while 奇数化偶数か
from random import randint

num1 =randint(1,49)
num2 = num1%2
count = 0
miss=0

while miss < 1:
  num1 =randint(1,49)
  num2 = num1%2
  
  if num2 == 0:
    check = str("偶数")
  else :
    check = str("奇数")
  
  judge = f"{num1}は奇数か偶数か？"
  value = input(judge)
  
  if (value == check):
    print("Good")
    count =count+1

  else :
    print("Not good")
    miss=1;
    
print("-"*20)  
print("good:",count,"回")