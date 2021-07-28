# https://www.codechef.com/problems/MUFFINS3

'''
Logic:
Chef has N cupcakes, and needs to decide how many cupcakes to place in each package. 
Each package must contain the same number of cupcakes. Chef will choose an integer 
A between 1 and N, inclusive, and place exactly A cupcakes into each package. 
Chef makes as many packages as possible. Chef then gets to eat the remaining cupcakes. 
Chef enjoys eating cupcakes very much. Help Chef choose the package size A that will let 
him eat as many cupcakes as possible.

T -> no of test cases
N -> no of cupcakes
'''

T = int(input())
l = []

for i in range(T):
    N = int(input())
    L = (N//2)+1
    l.append(L)

for j in l:
    print(j)