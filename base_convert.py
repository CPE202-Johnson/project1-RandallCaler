#two integers -> string
#Convert the base of a given value by integer b
def convert(num, b):
    """Recursive function that returns a string representing num in the base b"""
    lst = ["A", "B", "C", "D", "E", "F"]
    if num < b:
      remainder = num%b
      if remainder >= 10:
          remainder = lst[remainder-10]
      return str(remainder)
    if num >= b:
      if num//b >=1:
        quo = num//b
        remainder = num%b
        if remainder >= 10:
          remainder = lst[remainder-10]
        return (convert(quo, b) + str(remainder))
      