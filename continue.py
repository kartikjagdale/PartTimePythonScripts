#Filename:Continue.py
#running =True
while True:
    s=raw_input("Enter Something: ")
    if s=="Quit":
        break#Quit i.e Exit Loop
    if len(s)<3:
        print("Too Small")
        continue#continue the loop again i.e go Back and conitnue loop
    print("Input is of sufficient length")#print this statement if condtion is true
    print("The length of the input is :",len(s))#cpunt the length
  
