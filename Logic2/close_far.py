# Given three ints, a b c, return True if one of b or c is "close" (differing from a by at most 1), while the other is "far", differing from both other values by 2 or more. Note: abs(num) computes the absolute value of a number.

def close_far(a,b,c):
  diff_ab = abs(a-b)
  diff_ac = abs(a-c)
  diff_bc = abs(b-c)
  
  if diff_ab <= 1:
    if diff_ac >= 2 and diff_bc >= 2:
      return True
  elif diff_ac <= 1:
    if diff_ab >= 2 and diff_bc >= 2:
      return True
  return False


# another way, maybe better? 

def close_far(a, b, c):
    def is_close(x, y):
        return abs(x - y) <= 1
    
    def is_far(x, y):
        return abs(x - y) >= 2
    
    if (is_close(a, b) and is_far(a, c) and is_far(b, c)) or \
       (is_close(a, c) and is_far(a, b) and is_far(c, b)):
        return True
    return False

