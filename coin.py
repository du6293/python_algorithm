coin = [500,100,50,10]
N = 750 ##손님한테 거슬러 주어야 할 돈
cnt = 0
for i in coin:
    if N >= i:
        cnt += (N // i)
        a = N//i
        N = N-(a*i)
        
print(cnt)    
    



    



