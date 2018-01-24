# Return True if the string "cat" and "dog" appear the same number of times 
# in the given string.
def cat_dog(str):
  c_count=0
  d_count=0
  for i in range(len(str)-2):
    if str[i:i+3]=='cat':
      c_count+=1
    elif str[i:i+3]=='dog':
      d_count +=1
  return c_count==d_count