#FileName:Global_Statement.py
#if you are uing global statement in the function then the value of the variable of same name will chnage globally.

x = 50#local variable

def funct():
    global x
    print("value of local variable x is ",x)
    x=2
    print('value change of x in function is ',x)
    #end of function

funct()
print('after changing value of x in function globally value of X becomes ',x)
#End
    
