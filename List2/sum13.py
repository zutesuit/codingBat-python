# Return the sum of the numbers in the array, returning 0 for an empty array. Except the number 13 is very unlucky, so it does not count and numbers that come immediately after a 13 also do not count.

# originally did this with booleans:

def sum13(nums):
  totalSum = 0
  skip = False
  
  for num in nums:
    if skip:
      skip = False
      continue
    if num == 13:
      skip = True
      continue
    
    totalSum += num
    
  return totalSum
    


# another way, use a loop and increment index when it gets to 13, skipping it. 

def sum13(nums):
    total = 0
    i = 0
    while i < len(nums):
        if nums[i] == 13:
            i += 2
        else:
            total += nums[i]
            i += 1
    return total

