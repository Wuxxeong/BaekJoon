def makeone(n):
  DP=[0,0,1,1]
  for i in range(4, n+1):
    if i%6 == 0:
      DP.append(min(DP[i//3],DP[i//2],DP[i-1]) + 1)
    elif i%3 == 0:
      DP.append(min(DP[i//3],DP[i-1]) + 1)
    elif i%2 == 0:
      DP.append(min(DP[i//2],DP[i-1]) + 1)
    else:
      DP.append(DP[i-1] + 1)
  return DP[n]


X = int(input())
print(makeone(X))

'''
입력된 수를 1로 만들기 (DP)
'''