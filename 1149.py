def RGB():
  for i in range(1, N+1):
    for j in range(1,4):
      if j == 1:
        DP[i][j] = min(DP[i-1][2],DP[i-1][3]) + L[i-1][j-1]
      elif j ==2:
        DP[i][j] = min(DP[i-1][1],DP[i-1][3]) + L[i-1][j-1]
      elif j ==3:
        DP[i][j] = min(DP[i-1][1],DP[i-1][2]) + L[i-1][j-1]
  return min(DP[i][1], DP[i][2], DP[i][3])

N = int(input())
L = [list(map(int, input().split())) for i in range(N)]
DP = [[0]*4 for _ in range(N+1)]
print(RGB())