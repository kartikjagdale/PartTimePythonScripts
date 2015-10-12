#comapct the given array
a = [1,3,7,7,8,9,9,9,10]
n = len(a)
b= []

def compact(a,n):
    i=1;
    b.append(a[0]);
    while(i<n):
        if(a[i]!=a[i-1]):
            b.append(a[i]);
            i+=1;
        else:
            i+=1;
    return b,len(b);

print compact(a,n) 
