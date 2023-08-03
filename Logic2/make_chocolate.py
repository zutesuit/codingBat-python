# We want make a package of goal kilos of chocolate. We have small bars (1 kilo each) and big bars (5 kilos each). Return the number of small bars to use, assuming we always use big bars before small bars. Return -1 if it can't be done.

def make_chocolate(small, big, goal):
  maxBigBars = min(big, goal // 5)
  remainder = goal - (maxBigBars * 5)
  
  if remainder > small or remainder < 0:
    return -1
  else:
    return remainder
  
