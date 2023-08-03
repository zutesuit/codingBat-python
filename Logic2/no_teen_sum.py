# Given 3 int values, a b c, return their sum. However, if any of the values is a teen -- in the range 13..19 inclusive -- then that value counts as 0, except 15 and 16 do not count as a teens. Write a separate helper "def fix_teen(n):"that takes in an int value and returns that value fixed for the teen rule. In this way, you avoid repeating the teen code 3 times (i.e. "decomposition"). Define the helper below and at the same indent level as the main no_teen_sum().


# this is an interesting way of doing it - nesting the second function directly in the first so it ticks the boxes and passes the test n that. 

def no_teen_sum(a, b, c):
  def fix_teen(n):
    if n in [13, 14, 17, 18, 19]:
      return 0
    else:
      return n
      
  
  a = fix_teen(a)
  b = fix_teen(b)
  c = fix_teen(c)
  
  return a + b + c
    

# this ones neater a more defintion-strict solution:
def fix_teen(n):
    if (13 <= n <= 14) or (17 <= n <= 19):
        return 0
    return n

def no_teen_sum(a, b, c):
    return fix_teen(a) + fix_teen(b) + fix_teen(c)

