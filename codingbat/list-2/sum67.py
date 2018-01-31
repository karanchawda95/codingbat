
#Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 7 (every 6 will be followed #by at least one 7). Return 0 for no numbers.

def sum67(nums):
  flag = 1
  for i in range(len(nums)):
    if nums[i]==6:
       flag = 0
    while flag == 0:
      if nums[i] == 7:
        flag = 1
        nums[i] = 0
        break
      else:
        nums[i] = 0
      i+=1
  return sum(nums)