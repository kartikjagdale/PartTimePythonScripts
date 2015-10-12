"""from collections import defaultdict

n, m = map(int, raw_input().split());
d = defaultdict(list);

for i in range(0,n):
    d['A'].append(raw_input());
for i in range(0,m):
    d['B'].append(raw_input());

for position, item in enumerate(d['A']):
    for item2 in d['B']:
        if(item == item2):
            print position+1,
        else:
            print 1
    print('\n')

for i in range(m):
    for item in d['B']:
        print "item in B"+item
        if item in d['A']:
            print("item in A loop"+item)
            print(' '.join(map(str,d[item])));
        else:
            print('-1')
    

"""
#!/usr/bin/python
from collections import defaultdict
import sys
if sys.version_info[0]>=3: raw_input=input
N,M=map(int,raw_input().split())
d=defaultdict(list)
for i in range(N):
	s=raw_input().rstrip()
	d[s].append(i+1)
print d
for _ in range(M):
	s=raw_input().rstrip()
	if s in d:
		print(' '.join(map(str,d[s])))
	else:
		print('-1')

