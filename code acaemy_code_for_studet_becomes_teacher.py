#Filename :Code from Codeacaemy COders

Lloyd = {
    "name":"Lloyd",
    "homework": [90,97,75,92],
    "quizzes": [ 88,40,94],
    "tests": [ 75,90]
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

def average(stuff):
    return sum(stuff)/len(stuff)

def getLetterGrade(score):
    score = round(score)
    if  score >= 90: return "A"
    elif  90 > score >= 80: return "B"
    elif  80 > score >= 70: return "C"
    elif  70 > score >= 60: return "D"
    elif  60 > score: return "F"

def getAverage(kid):
    bar = average
    return bar(kid["homework"])*.1 + bar(kid["quizzes"])*.3 + bar(kid["tests"])*.6

def getClassAverage(kids):
    total = 0
    for kid in kids:
        total = total + getAverage(kid)
    return total/len(kids)
print getAverage(Lloyd)

print getLetterGrade(getAverage(Lloyd))

students = [Lloyd,Alice,Tyler]
print getClassAverage(students)



