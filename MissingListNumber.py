list = [0,1,6,5,4,3]

def MissingListNumber(list):
    n = len(list)
    s = n(n+1)/2
    num = 0
    for i in range(0,n):
        num += list[i]
    ans = s-num
    return ans

print(MissingListNumber(list))
