# Multplication algorithm (a La russe )
# From Book Fundamentals of Algorithmics

def russe(m,n):
    result = 0
    while(m>0): #Loop Until the multiplier becomes "1"
        flag = False
        if(m%2!=0): # check if odd or not
            result=result+n # if yes add the value of n to result
            flag = True
        if(flag ==True): # used for printing step by step
            print m,"\t",n,"\t",n 
        else:
            print m,"\t",n,"\t"
        m=m/2 #Divide Multiplier by 2 (yes until it becomes "1" )
        n=n+n # Double the value of Multiplicand
        
        
    return result


x = int(raw_input("Enter Multiplier: "))
y = int(raw_input("Enter Multiplicand: "))

total = russe(x,y) #call the function

print "*"*25
print "\t\t",total
print "\n Multiplication is ",total

#************************OUTPUT**********************#
Output = """
Enter Multiplier: 981
Enter Multiplicand: 1234
981 	1234 	1234
490 	2468 	
245 	4936 	4936
122 	9872 	
61 	19744 	19744
30 	39488 	
15 	78976 	78976
7 	157952 	157952
3 	315904 	315904
1 	631808 	631808
*************************
		1210554

Multiplication is  1210554
"""
