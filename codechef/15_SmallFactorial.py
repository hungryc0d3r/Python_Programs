# https://www.codechef.com/problems/FLOW018
# same as 8
T = int(input())
Fl = []
for i in range(T):
    N = int(input())
    fact = 1
    for j in range(1,N+1):
        fact *= j
    Fl.append(fact)

for k in Fl:
    print(k)
    