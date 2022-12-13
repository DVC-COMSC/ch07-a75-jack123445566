num1 = input("Enter the elements of list num1 separated by space: ").split()
num2 = input("Enter the elements of list num2 separated by space: ").split()

num1 = [int(i) for i in num1]
num2 = [int(i) for i in num2]


if all(i in num2 for i in num1):
  
  if num2.index(num1[0]) + len(num1) <= len(num2):
    
    if num2[num2.index(num1[0]):num2.index(num1[0])+len(num1)] == num1:
      print(True)
    else:
      print(False)
  else:
    print(False)
else:
  print(False)
