# Given two strings, return True if either of the strings appears at the very 
# end of the other string, ignoring upper/lower case differences (in other 
# words, the computation should not be "case sensitive").

def end_other(a, b):
  xa=len(a)
  xb=len(b)
  a = a.lower()
  b = b.lower()
  if a[-xb:]==b:
    return True
  if b[-xa:]==a:
    return True
  else:
    return False

#or

def end_other(a, b):
    a = a.lower()
    b = b.lower()
        
    return a.endswith(b) or b.endswith(a)