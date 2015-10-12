#Quora Answer

num = raw_input("Enter a three  digit number: ")

for i in range(0,3):
    if(int(num[i])%2==0):
        print 'E', #Even 
    else:
        print 'O', #Odd
        
"""
OUTPUT:
>>Enter a three  digit number: 369
>>O E O

"""
