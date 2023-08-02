# Given a string, return a new string made of every other char starting with the first, so "Hello" yields "Hlo".

def string_bits(str):
  return str[0::2]

# other way just to write a bit more

def string_bits(str):
  final = ""

  for i in range(len(str)):
    if i % 2 == 0:
      final = final + str[i]

  return final
