Given 3 int values, a b c, return their sum. However, if one of the values is 13 then it does not count towards the sum and values to its right do not count. So for example, if b is 13, then both b and c do not count.

# simple

def lucky_sum(a, b, c):
  if a == 13:
    return 0
  elif b == 13:
    return a
  elif c==13:
    return b + a
  else:
    return a + b + c

# little more complex

def lucky_sum(a, b, c):
    values = [a, b, c]
    if 13 in values:
        index = values.index(13)
        return sum(values[:index])
    else:
        return sum(values)


# loop

def lucky_sum(a, b, c):
    total = 0

    for n in (a, b, c):
        if n != 13:
            total += n
        else:
            break

    return total


