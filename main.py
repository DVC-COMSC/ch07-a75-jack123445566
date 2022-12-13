

num1 = list(map(int, input("Enter the elements of num1 separated by space: ").split()))
num2 = list(map(int, input("Enter the elements of num2 separated by space: ").split()))


if all(x in num2 for x in num1):
    
    for i in range(len(num1)):
        if num1[i] != num2[i]:
            print("False")
            break
    else:
        print("True")
else:
    print("False")
