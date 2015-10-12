# Enter your code here. Read input from STDIN. Print output to STDOUT
L = [];
N = int(raw_input());

while(0<N):
    user = [];
    user.append(raw_input().split());
    if(len(user[0])== 3):
       if(user[0][0]=='insert'):
           L.insert(int(user[0][1]), int(user[0][2]));
    elif(len(user[0])== 2):
        if(user[0][0]=='remove'):
            L.remove(int(user[0][1]));
        if(user[0][0]=='append'):
            L.append(int(user[0][1]));
    elif(len(user[0])== 1):
        if(user[0][0]=='print'):
            print L
        if(user[0][0]=='pop'):
            L.pop()
        if(user[0][0]=='sort'):
            L.sort();
        if(user[0][0]=='reverse'):
            L.reverse()
    N -=1;
