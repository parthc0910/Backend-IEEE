def findPairs(lst, K): 
    res = []
    while lst:
        num = lst.pop()
        diff = K - num
        if diff in lst:
            res.append((diff, num))
         
    res.reverse()
    return res

a = int(input("Enter the number of elements"))   
lst = []

while(a>0):
    b = int(input())
    lst.append(b)
    a=a-1
    
K = int(input("Enter the target : "))
print(findPairs(lst, K))
