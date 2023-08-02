# Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 7 (every 6 will be followed by at least one 7). Return 0 for no numbers.


def sum67(nums):
  total = 0
  ignore = False
  
  for num in nums:
    if num == 6:
      #while num != 7:
        ignore = True
        continue
    if ignore:
      if num == 7:
        ignore = False
      continue  
      
    
    total = total + num
      
  return total
    
  

