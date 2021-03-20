n,m,k = map(int, input().split())
data = list(map(int ,input().split()))

data.sort()

max_value = data[n-1];
second_value = data[n-2];

result = 0;

while True:
  for i in range(k):
    if m==0:
      break
    result+=max_value
    m-=1
  if m==0:
    break
  result+=second_value
  m-=1
print(result)
