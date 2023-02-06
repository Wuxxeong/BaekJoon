def num(n):
  DP = [0,1,2,4]
  for i in range(4, n+1):
    DP.append(DP[i-1]+DP[i-2]+DP[i-3])
  return DP[n]

T = int(input())
for _ in range(T):
  X = int(input())
  print(num(X))