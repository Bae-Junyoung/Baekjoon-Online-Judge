S = input()
P = input()

def func(S,P):
    p = [0] * len(P)
    lengthP = len(P)
    lengthS = len(S)
    
    j=0
    for i in range(1,lengthP):
        while j>0 and P[i]!=P[j]:
            j = p[j-1]
            
#         print(i,j)
        if P[i]==P[j]:
            j+=1
            p[i]=j
    
#     p = [-1] + p

    j = 0
    for i in range(lengthS):
        while j > 0 and S[i] != P[j]:
            j = p[j - 1]

        if S[i] == P[j]:
            if j == lengthP - 1:
                return 1
            else:
                j += 1
    return 0
print(func(S,P))