''' Given an array a of size n, find the XOR of all subarrays' XORs. 
The subarray XOR is the XOR of all elements in a subarray. Return the total XOR obtained.  '''


n=int(input())
a=list(map(int,input().split()))
result=0
for i in range(n):
  sub=0
  for j in range(i,n):
    sub ^= a[j]
    result ^= sub
print(result)
