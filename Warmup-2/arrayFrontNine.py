# Given an array of ints, return True if one of the first 4 elements in the array is a 9. The array length may be less than 4.

def array_front9(nums)
  length = len(nums)
  if length > 4:
    length = 4 # only conuting first 4 so rest art irrelevant
    
  for i in range(length):
    if nums[i] == 9:
      return True
      
  return False

# but got to do better than that usually, the best way is just seeking through the index in a return statement:

def array_front9(nums)
  return 9 in nums[:4]
