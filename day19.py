import time
begin=time.time()

"""
	Choosing the  right data structure helps a lot.
  Source : subreddit/adventofcode/
  This code belong to some other user.
"""

class Node:
  def __init__(self,id):
    self.id  = id
    self.nxt = None
    self.prv = None

  def delete(self):
    self.prv.nxt = self.nxt
    self.nxt.prv = self.prv

def solve(n):
  l = map(Node, xrange(n))

  for i in xrange(n):
    l[i].nxt = l[(i+1)%n]
    l[i].prv = l[(i-1)%n]

  start = l[0]
  mid   = l[n/2]

  for i in xrange(n-1):
    mid.delete()
    mid = mid.nxt
    if (n-i)%2==1: mid = mid.nxt
    start = start.nxt

  return start.id+1

print solve(3012210)
print time.time()-begin