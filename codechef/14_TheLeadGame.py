# https://www.codechef.com/problems/TLG

'''
Logic:
no of rounds -> N
W -> Winner
L -> Lead 
initial -> P1  0 P2  0 L   0 W   0
next    -> P1 = P1+P1s and P2 = P2+P2s
difference = |P1 - P2|
if difference > Lead => Lead = difference
(if diff > Lead in another to means we need to add that P1s and P2s upto that round
then we need to find difference)
if P1 > P2 => W=1
if P1 < P2 => W=2
'''
N = int(input())

W = 0
L = 0
P1 = 0
P2 = 0
for R in range(N):
    P1s, P2s = map(int, input().split())
    P1 += P1s
    P2 += P2s
    diff = abs(P1 - P2)
    if (diff > L):
        L = diff
        if (P1 > P2):
            W = 1
        else:
            W = 2
print(W, L)
