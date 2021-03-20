#방법1

n,m,k = map(int,input().split())

data = list(map(int,input().split()))
first = data[n-1]
second = data[n-2]

result = 0

while True:
  for i in range(K):
    if m == 0:
      break
    result+=first
    m-=1
   if m == 0:
    break
   result+=second
   m-=1
print(result)

#방법
n,m,k = map(int,input().split())
data = list(map(int,input().split()))

data.sort()
first = data[n-1]
second = data[n-2]

#가장큰수가 더해지는 횟수 계산
count = int(m/(k+1))*k
count += m%(k+1)
result = 0
result += (count)*first
result +=(m-count)*second
print(result)

