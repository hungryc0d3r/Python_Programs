# https://www.codechef.com/problems/FLOW008

T = int(input())
O = []

for i in range(T):
    N = int(input())
    if N < 10:
        Out = "Thanks for helping Chef!" 
    else:
        Out = '-1'
    O.append(Out)    
    
for j in O:
    print(j)