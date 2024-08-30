A= []

print("Enter the numbers")

i = 5
while(i>0):

    b = int(input())
    A.append(b)
    i = i-1

def Greatest_Common_Divisor(A):
    for c in A:
        while int(c) > 0:
            if int(c) > 12:
                c = int(c) % 12
            else:
                return 12 % int(c)
print(Greatest_Common_Divisor(A))
