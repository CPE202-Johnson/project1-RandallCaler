#two integers -> string
def convert(num, b):
    """Recursive function that returns a string representing num in the base b"""
    if num == 0:
      remainder = num%b
      print(remainder)
    if num > 0:
      if num//b >=1:
        quo = num//b
        print(num%b)
        return convert(quo, b)
      