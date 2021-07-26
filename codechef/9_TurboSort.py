# https://www.codechef.com/problems/TSORT

'''Given the list of numbers, you are to sort them in non decreasing order.

Input
t – the number of numbers in list, then t lines follow [t <= 10^6].
Each line contains one integer: N [0 <= N <= 10^6]

Output
Output given numbers in non decreasing order.'''

t = int(input())
TS = []

for i in range(t):
    n = int(input())
    TS.append(n)

TS.sort()
for j in TS:
    print(j)
    
    