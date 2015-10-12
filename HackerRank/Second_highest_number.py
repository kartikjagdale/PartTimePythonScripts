#Find Second Highest Number
N = int(raw_input());
numbers = sorted(map(int, raw_input().split()), reverse=True);
print numbers
for i in range(len(numbers)):
    try:   
        if(numbers[i] == numbers[i+1]):
            continue;
        print numbers[i+1];
        break;
    except IndexError:
        break;
        

