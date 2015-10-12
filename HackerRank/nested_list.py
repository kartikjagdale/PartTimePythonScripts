#nested List:
N = int(raw_input()); #Take Number of Students
lis = [];

for i in range(N): #Get Student Names and Marks
    lis.append([raw_input(),float(raw_input())]);
#Find The Second Highest Students Marks
try:
    second_highest = sorted(list(set([marks for name, marks in lis])))[1]
except IndexError:
    second_highest = lis[0][1]; # if there us only one student or all students with same marks
#Store Names of Second Highest Students
Names = [name for name, marks in sorted(lis) if marks == second_highest]

for name in Names:
    print name
