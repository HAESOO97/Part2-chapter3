n, k = map(int,input().split())

result = 0
while n>=k:
  while n%k!=0:
    n-=1
  n//=k
  result +=1
while n>1:
  n-=1
  result+=1
print(result)
#방법2
n,k  = map(int,input().split())

result = 0
while True:
  #(N==K)로 나누어떨어지는 수가 될때까지 1씩 빼기
  target = (n//k)*k
  result+=target
  n = target
  if n<k:
    break
  result+=1
  n//=k
  
result +=(n-1)
print(result)
