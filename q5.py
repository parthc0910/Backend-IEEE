a =[[1,2,3,4],[1,2,4,5],[1,3,4,5],[2,3,5],[1,2,3]]

i = 0

cta1 = 0
cta2 = 0
cta3 = 0
cta4 = 0
cta5 = 0

while(i<5):

    j = 0
    
    b = len(a[i])
    while(b>j):
        
        if(a[i][j] == 1):
            cta1 = cta1 + 1

        if(a[i][j] == 2):
            cta2 = cta2 + 1

        if(a[i][j] == 3):
            cta3 = cta3 + 1

        if(a[i][j] == 4):
            cta4 = cta4 + 1

        if(a[i][j] == 5):
            cta5 = cta5 + 1
        j = j+1

    i = i+1
    
b = [cta1,cta2,cta3,cta4,cta5]
b.sort()

print(b)

while(i<5):

    a






