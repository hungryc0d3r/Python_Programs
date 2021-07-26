# https://www.codechef.com/problems/LUCKFOUR

'''Kostya likes the number 4 much.
Impressed by the power of this number, Kostya has begun to look for occurrences of 
four anywhere. He has a list of T integers, for each of them he wants to calculate 
the number of occurrences of the digit 4 in the decimal representation. He is too busy
now, so please help him.

Input
The first line of input consists of a single integer T, denoting the number of integers 
in Kostya's list.

Then, there are T lines, each of them contain a single integer from the list.

Output
Output T lines. Each of these lines should contain the number of occurences of the digit 
4 in the respective integer from Kostya's list.'''

T = int(input())

LF = []

for i in range(T):
    N = int(input())
    count = 0
    while N!=0:
        if N%10 == 4:
            count += 1
        N = N//10
    LF.append(count)

for j in LF:
    print(j)
    
    