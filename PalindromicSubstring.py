#Length of longest palindromic substring
s=input()
n=len(s)
d=[[0] * n for _ in range(n)]
for i in range(n):
  d[i][i]=1
l=1
f=0
for i in range(n-1):
  if s[i]==s[i+1]:
    d[i][i+1]=1
    f=i
    l=2
for k in range(3,n+1):
  for i in range(n-k+1):
    j=i+k-1
    if d[i+1][j-1] and s[i]==s[j]:
      d[i][j]=1
      f=i
      l=k
print(l)
