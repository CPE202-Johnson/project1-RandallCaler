#string -> list of strings
#Retruns list of permutations for a given string
def perm_gen_lex(a): 
    strlist = []
    if a == None:
      raise ValueError("Empty List")
    if len(a) == 0:
      return []
    if len(a) == 1:
      return [a]
    for num in range(len(a)):
      newstr = a[:num] + a[num+1:]
      newlist = perm_gen_lex(newstr)
      for val in newlist:
        newval = a[num]+val
        strlist.append(newval)
    return strlist

 