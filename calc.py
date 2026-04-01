#to perform basic arithmetic operations
a=int(input("enter the value of a:"))
b=int(input("enter the value of b:"))
choice=int(input("enter the choice:1-add,2=sub,3=mul,4=div:"))
if choice == 1:
    print("The sum is:",a+b)
elif choice == 2:
    print("The difference is:",a-b)
elif choice == 3:
    print("The product is:",a*b)
elif choice == 4:
    print("The quotient is:",a/b)
else:
    print("Invalid!")