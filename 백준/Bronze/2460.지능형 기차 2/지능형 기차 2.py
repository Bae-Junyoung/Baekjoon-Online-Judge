M = 0
train = 0

for _ in range(10):
    t_out, t_in = list(map(int,input().split()))
    train = train - t_out + t_in
    
    if train >= M:
        M = train
        
print(M)