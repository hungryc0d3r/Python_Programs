# https://www.codechef.com/problems/AMR15A

'''
Logic:
Even lucky -> Ready for battle
Odd Unlucy -> Not Ready
'''

N = int(input())
Sol = list(map(int, input().split()))
L=0
U=0
    
for j in range(N):
    if Sol[j] % 2 == 0:
        L+=1
    else:
        U+=1

if L>U:
    print('READY FOR BATTLE')
else:
    print('NOT READY')
