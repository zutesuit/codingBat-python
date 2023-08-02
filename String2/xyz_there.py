# Return True if the given string contains an appearance of "xyz" where the xyz is not directly preceeded by a period (.). So "xxyz" counts but "x.xyz" does not.

# can do this the loopy way:

def xyz_there(str):
    for i in range(len(str) - 2):
        if str[i:i+3] == "xyz" and (i == 0 or str[i-1] != '.'):
            return True
    return str[:3] == "xyz"


# but I think this is best way:

def xyz_there(str):
  str = str.replace(".xyz", "") #remove it altogether so only instances of the string that contain 'xyz' will show up. 
  return "xyz" in str
