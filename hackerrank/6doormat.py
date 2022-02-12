"""
Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door mat with the following specifications:
Mat size must be X. ( is an odd natural number, and  is  times .)
The design should have 'WELCOME' written in the center.
The design pattern should only use |, . and - characters.
"""

""" 
-------- Output ---------
Size: 7 x 21                   # stdin
    ---------.|.---------      # stdout
    ------.|..|..|.------
    ---.|..|..|..|..|.---
    -------WELCOME-------
    ---.|..|..|..|..|.---
    ------.|..|..|.------
    ---------.|.---------
"""

# method - 1
# Enter your code here. Read input from STDIN. Print output to STDOUT 
N, M = (int(x) for x in input().split())

pattern = [(('.|.'*(2*i+1)).center(M, '-')) for i in range(N//2)]
pattern2 = [(('.|.'*(2*(N//2 - i)-1)).center(M, '-')) for i in range(N//2)]
    
print('\n' .join(pattern + ["WELCOME".center(M, '-')] + pattern2))

# method 2
for i in range(N//2):
    print(('.|.'*(2*i+1)).center(M, '-'))
    
print("WELCOME".center(M, '-'))

for j in range(N//2):
    print(('.|.'*(2*(N//2 - j)-1)).center(M, '-'))
    
