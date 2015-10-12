#No Idea
from collections import Counter
n , m = map(int, raw_input().split());
numbers = Counter(map(int,raw_input().split())[:n]);
A = map(int, raw_input().split())[:m]
B = map(int, raw_input().split())[:m]
Happy = 0;
for key in numbers:
    if key in A:
        Happy += numbers[key];
    elif key in B:
        Happy -= numbers[key]
print(Happy);
