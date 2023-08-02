# Given a non-empty string like "Code" return a string like "CCoCodCode"

def string_splosion(str):
  # so change string to 1st char plus 1st char then 2nd char plaus 1st char then second and third etc
  splos = ""
  for i in range(len(str)):
    splos = splos + str[:i+1]
  return splos

