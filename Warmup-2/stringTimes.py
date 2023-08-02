# Given a string and a non-negative int n, return a larger string that is n copies of the original string.

def string_times(str, n)
  return str * n

# much longer way just because:

def string_times(str, n):
  stringy = ""
  for i in range(n):  
    stringy = stringy + str 
  return stringy
