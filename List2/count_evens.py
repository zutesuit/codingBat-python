# Return the number of even ints in the given array. Note: the % "mod" operator computes the remainder, e.g. 5 % 2 is 1.

def count_evens(nums):
  evensCount = 0
  for num in nums:
    if num % 2 == 0:
      evensCount += 1
  
  return evensCount

# different way:

def count_evens(nums):
  return sum(1 for num in nums if num % 2 == 0)

  
