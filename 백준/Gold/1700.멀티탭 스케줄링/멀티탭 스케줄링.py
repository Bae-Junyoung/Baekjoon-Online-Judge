N, K = map(int, input().split())

equips = list(map(int, input().split()))

answer = 0

multap = [0] * N
change = 0

for i in range(K):
    max_index = 0
    if equips[i] in multap:
        pass
    elif 0 in multap:
        multap[multap.index(0)] = equips[i]
    else:
        length = multap.copy()
        for x in multap:
            if x not in equips[i+1:]:
                change = x
                break
            else:
                max_index =  max(equips[i+1:].index(x), max_index)
                change = equips[i+1:][max_index]
        
        multap[multap.index(change)] = equips[i]
        answer+=1

print(answer)