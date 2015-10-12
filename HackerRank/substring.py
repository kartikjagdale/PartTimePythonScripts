string = raw_input();
substring = raw_input();
sublen = len(substring);
count = 0;
for i in range(len(string)):
    if(string[i] == substring[0]):
        if(string[i:i+sublen] == substring):
            count += 1;
print count
       
