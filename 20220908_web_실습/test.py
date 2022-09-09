n,m = map(int,input().split())
cnt = 0
for _ in range(m):
  d = int(input())
  d_list = list(map(int, input().split()))
  for i in range(d-1):
    if d_list[i]>d_list[i+1]:
      pass
    else:
      cnt+=1

if cnt == 0:
  print('yes')
else:
  print('no')