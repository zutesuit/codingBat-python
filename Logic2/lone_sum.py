# Given 3 int values, a b c, return their sum. However, if one of the values is the same as another of the values, it does not count towards the sum.


#obvious way:

def lone_sum(a, b, c):
  if a == b == c:
    return 0
  elif a == b:
    return c
  elif a == c:
    return b
  elif b == c:
    return a
  else:
    return a+b+c
    

# there's this cool way to do it though:

def lone_sum(a, b, c):
    unique_values = {a, b, c}
    return sum(x for x in unique_values if [a, b, c].count(x) == 1)

