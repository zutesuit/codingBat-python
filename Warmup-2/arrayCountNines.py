# Given an array of ints, return the number of 9s in the array. 



def array_count9(nums):
    count = 0
    for num in nums:
        if num == 9:
            count += 1
    return count

# but obvious way in python is to check for appropriate method and just use that:

def array_count0(nums):
  return nums.count(9)
