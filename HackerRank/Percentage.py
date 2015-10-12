# Enter your code here. Read input from STDIN. Print output to STDOUT
#Percentage
from __future__ import division
Stud = {}
num = int(raw_input());
for i in range(0, num):
    name, maths, physics, chemistry = raw_input().split(' ')
    Stud[name] = [float(maths), float(physics), float(chemistry)];


userinput = raw_input();
if(userinput in Stud):
    total = 0;
    for item in Stud[userinput]:
        total += item
    print("%.2f"%((total/300) * 100))
    
