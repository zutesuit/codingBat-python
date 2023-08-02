# Given an array of ints, return True if the sequence of numbers 1, 2, 3 appears in the array somewhere.

def array123(nums):
  return any(nums[i:i+3] == [1, 2, 3] for i in range(len(nums) - 2))

# but if any() not available for some reason:

  for i in range(len(nums)-2):
    if nums[i]==1 and nums[i+1] == 2 and nums[i+2] == 3:
      return True
  return False
