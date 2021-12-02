import math

def scrap_validator(q, min_price, max_price, reverse, update_tolerance):
  q = __validate_q(q)
  min_price = __validate_min_price(min_price)
  max_price = __validate_max_price(max_price)
  reverse = __validate_reverse(reverse)
  update_tolerance = __validate_update_tolerance(update_tolerance)
  return q, min_price, max_price, reverse, update_tolerance

def __validate_q(q):
  if q == None or q == False:
    return ""
  return q

def __validate_min_price(min_price):
  if min_price == '' or min_price == None or min_price == False:
    return 0.0
  try:
    return float(min_price)
  except:
    return 0.0

def __validate_max_price(max_price):
  if max_price == '' or max_price == None or max_price == False:
    return math.inf - 1
  try:
    return float(max_price)
  except:
    return math.inf - 1

def __validate_reverse(reverse):
  if reverse == '' or reverse == None or reverse == False:
    return False
  elif reverse == "true":
    return True
  else:
    return False

def __validate_update_tolerance(update_tolerance):
  if update_tolerance == '' or update_tolerance == None or update_tolerance == False:
    return False
  try:
    return int(update_tolerance)
  except:
    return False