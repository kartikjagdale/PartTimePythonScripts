#set
N = int(raw_input());
set1 = set(map(int, raw_input().split()));
M = int(raw_input());
set2 = set(map(int, raw_input().split()));
diff1 = set1.difference(set2)
diff2 = set2.difference(set1)
final = sorted(list(diff2.union(diff1)));
for i in range(len(final)):
    print final[i]
    

