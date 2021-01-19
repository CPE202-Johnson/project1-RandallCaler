#number -> boolean
#Given a certain integer, declares True or False if said number reaches a specific goal
def bears(n):
    #base cases
    if n == 42:
        return True
    if n < 42:
        return False
    #When it's divisible by 2
    if n%2 == 0:
        if bears(n/2) is True:
            return True
    #When it's divisible by 3 or 4
    if n%3 == 0 or n%4 == 0:
        temp1 = int(n/10)
        temp2 = int(n%10)
        if temp1 != 0 and temp2 != 0:
          if bears(n - temp1*temp2) is True:
              return True
    #When it's divisible by 5
    if n%5 == 0:
        if bears(n-42) is True:
            return True
    else:
        return False