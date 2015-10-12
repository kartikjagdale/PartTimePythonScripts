#Filename: Compare.py

def maxi(a,b):#define maxi function
    if a>b:
        print(a,"is maximum")
    elif a==b:
        print("Both are Equal")
    else:
        print(b,"is Greater")
        #End of Function
while True:#Loop Started
    g=int(input("What You Want to Do?\n1:Enter\n2:Exit\n="))#User Conformation
    if g==1:
        x=int(input('Enter any Value'));y=int(input('Enter anotehr value'));maxi(x,y)#user Value Input and operation
        continue
    elif g==2:#exit
        break
    else:
        print("You Enterd Wrong Choice,Please Enter Again")#wrong Choice and loop continues
        continue
    #End of Loop
print('*'*3,"Thank You",'*'*3,) #Exit Statement   
#end

        
        
