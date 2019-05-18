def check_pattern(str_value):
  str_len = round(len(str_value)/2)
  start_str = str_value[0:str_len]
  print(start_str)
  end_str = str_value[str_len: len(str_value)]
  print(end_str)
  if start_str == end_str :
    return True
  return False

print(check_pattern('123123'))