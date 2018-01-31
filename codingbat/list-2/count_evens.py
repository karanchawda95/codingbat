#Return the number of even ints in the given array. Note: the % #"mod" operator computes the remainder, e.g. 5 % 2 is 1.
def count_evens(nums):
  even_count=0
  for i in range(len(nums)):
    if nums[i]%2==0:
      even_count+=1
  return even_count