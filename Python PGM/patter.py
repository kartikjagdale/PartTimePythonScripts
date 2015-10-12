#Searching for Patterns | Set 1 (Naive Pattern Searching)



def search(pat, txt):
    print "In search fun"
    M = len(pat)
    N = len(txt)

    for i in range(0,N-M):
        #print "value of I is ",i
        j = 0
        while(j<M):
            if(txt[i+j]!=pat[j]):
                break;
            j+=1
        #print "J is ",j
        if(j==M):
            print "Pattern found at index %u \n"%(i)
            
    


txt = "AABAACAADAABAAABAA"
pat = "AABA"
search(pat, txt)
