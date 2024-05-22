
def maxSubArray(a,l):
    maxval=float('-inf')
    for i in range(len(a)):
        sum=0
        
        for j in a[i:i+l]:
            sum+=j

        if len(a[i:i+l])==4 and maxval<=sum:
            maxval=sum
            res=a[i:i+l]
    return maxval,res

l=[3,-1,4,-2,4,-7,0,12]
print(list(maxSubArray(l,4)))
