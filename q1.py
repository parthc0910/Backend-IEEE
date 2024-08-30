a = input("Enter a string")
b = input("Enter another string")

i = len(a)
co =0

while(i>0):
    j = len(b)
    while(j>0):
        if(a[i-1] == b[j-1]):
            co = co+1

        j = j-1
    i = i-1
    
if (co >0):
    print("The strings are complemontary")
else: 
    print("The string are not complementory")