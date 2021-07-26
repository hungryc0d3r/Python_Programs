# https://www.codechef.com/problems/INTEST

'''The purpose of this problem is to verify whether the method you are using to read input data 
is sufficiently fast to handle problems branded with the enormous Input/Output warning. You are 
expected to be able to process at least 2.5MB of input data per second at runtime.

Input
The input begins with two positive integers n k (n, k<=10^7). 
The next n lines of input contain one positive integer ti, not greater than 10^9, each.

Output
Write a single integer to output, denoting how many integers ti are divisible by k.'''

n = int(input('n = '))
k = int(input('k = '))

count = 0

for i in range(n):
    ti = int(input())
    if ti % k == 0:
        count += 1

print(count)

