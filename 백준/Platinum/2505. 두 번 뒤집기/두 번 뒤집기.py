from itertools import *

def find(seq):
  start=0
  end=0
  for i in range(N+1):
    if i!=seq[i]:
      if not start:
        start=i
      end = i
  return (start,end) if start else (1,1)

def reverse(seq,start,end):
  return seq[:start]+[*reversed(seq[start:end+1])]+seq[end+1:]

N = int(input())
seq = [0]+[*map(int,input().split())]

start,end = find(seq)

gap = []; s = start
while s<=end:
  gap.append(s)
  e = s
  while e<end:
    if abs(seq[e+1]-seq[e])==1:
      e += 1
    else:
      break
  gap.append(e)
  s = e+1
  
seq0 = [i for i in range(N+1)]
for s,e in combinations(gap,2):
  s1,e1 = min(s,e),max(s,e)
  seq1 = reverse(seq,s1,e1)
  s2,e2 = find(seq1)
  if reverse(seq1,s2,e2)==seq0:
    result = [(s1,e1),(s2,e2)]
for s,e in result:
  print(s,e)