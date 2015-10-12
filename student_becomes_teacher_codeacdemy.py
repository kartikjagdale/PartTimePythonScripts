#Filename:Student Becomes Teacher
#course:Codeacaemy

Lloyd = {
    "name":"Lloyd",
    "homework": [90,97,75,92],
    "quizzes": [88,40,94],
    "tests": [75,90]
    }
Alice = {
    "name":"Alice",
    "homework": [100,92,98,100],
    "quizzes": [82,83,91],
    "tests": [89,97]
    }
Tyler = {
    "name":"Tyler",
    "homework": [0,87,75,22],
    "quizzes": [0,75,78],
    "tests": [100,100]
    }
    
students=[Lloyd,Alice,Tyler]

for key in students:
    print "\t",key["name"] #name
    print key["homework"]
    print key["quizzes"]
    print key["tests"]

def average(lst):
    print "Average of",lst["name"],"is:"
    return sum(lst["homework"]+lst["quizzes"]+lst["tests"])/len(lst["homework"]+lst["quizzes"]+lst["tests"])
print average(Alice)

def average1(scores):
    return int(sum(scores) /len(scores))

print average(Lloyd)



