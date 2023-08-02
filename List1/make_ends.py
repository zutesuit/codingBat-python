# Given an array of ints, return a new array length 2 containing the first and last elements from the original array. The original array will be length 1 or more.

def make_ends(nums):
  return [nums[0], nums[-1]]

# very slightly differently:

def make_ends(nums):
  return nums[:1] + nums[-1:]

# noting that slicing creates lists with one element each, which can then be concatenated. 
