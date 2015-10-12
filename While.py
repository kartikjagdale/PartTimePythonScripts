#FileName: While.py

num=23
running=True

while running:
    guess=int(input("Enter any Number: "))

    if guess==num:
        print("Congo you WIN")
        running=False
    elif guess<num:
         print("Little Higher")
    else:
         print("little Lower")
print("Finish")         
