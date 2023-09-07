N,M = map(int,input().split()) # N과 M 을 공백을 두고 입력받는다.
basket = [i for i in range(1, N+1)]
for i in range(M):
    i,j = map(int, input().split())
    temp = basket[i-1:j]
    temp.reverse()
    basket[i-1:j]=temp

for i in range(N):
    print(basket[i],end="")
