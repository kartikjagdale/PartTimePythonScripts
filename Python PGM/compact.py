#comapct the given array

a = [1,3,7,7,8,9,9,9,10]
n = len(a)
b= []
def comapct(a,n):
    ins = 1;
    for i in xrange(1,n):
        if(a[i]!=a[ins-1]):
            a[ins]=a[i];
            b.append(a[i]);
            i+=1
            ins+=1
        else:
            i+=1;
    return b,len(b);
print comapct(a,n)

    


