cases = int(input())
returnList = []

while(cases>0):
    cases-=1
    a,b,n,s = input().split()
    a = int(a) # number of coins of value n | 1
    b = int(b) # number of coins of value 1 | 2
    n = int(n) # value n | 3
    s = int(s) # value to be reached | 4
    num = (a*n) + b
    check = s%n
    if(num>=s and b>=check):
        print("YeS")
    else:
        print("nO")

'''
End of code!!!
Date started: 11/21/2019
Date ended: 11/22/2019
Time spent: 45 minutes
Codeforces problem: 1256A
'''
