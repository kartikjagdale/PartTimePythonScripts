#Filename:Switch statement Implementation Using While
num1=int(input("Enter 1st Numebr: "))
num2=int(input('Enter 2nd Number: '))
print("Welcome\n Choose an Option\n 1:Addition\n 2:Substraction\n 3:Multiplication\n 0:Exit")
running =True

while running:
    choice=int(input("Enter Your Choice: "))

    if choice==1:
        print("Addition is :",num1+num2)
    elif choice==2:
        print("Substraction is: ",num1-num2)
    elif choice==3:
        print("Multiplication is: ",num1*num2)
    elif choice==0:
        break
    elif choice!=1&choice!=2&choice!=3:
        print("Wrong Choice Please Select Again")
        continue
        #running=False
    else:
        print("bye")
print("Thank You !")
