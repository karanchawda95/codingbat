#Return the "centered" average of an array of ints, which we'll say #is the mean average of the values, except ignoring the largest and #smallest values in the array. If there are multiple copies of the #smallest value, ignore just one copy, and likewise for the largest #value. Use int division to produce the final average. You may #assume that the array is length 3 or more.

def centered_average(nums):
  Nums = sorted(nums)
  Nums.pop(0)
  Nums.pop(-1)
  smallest,largest = min(nums),max(nums)
  count,sum=0,0
  for i in range(len(Nums)):
    sum+=Nums[i]
    count+=1
  return sum/count