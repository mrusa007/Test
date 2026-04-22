#simple calculator
num1=int(input("Enter First Number: "))
num2=int(input("Enter Second Number: "))
print("Select Operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
choice=int(input("Enter Choice(1/2/3/4): "))
if choice==1:
    print(num1,"+",num2,"=",num1+num2)
elif choice==2:
    print(num1,"-",num2,"=",num1-num2)
elif choice==3: 
    print(num1,"*",num2,"=",num1*num2)
elif choice==4:
    print(num1,"/",num2,"=",num1/num2)
else:   
    print("Invalid Input")
