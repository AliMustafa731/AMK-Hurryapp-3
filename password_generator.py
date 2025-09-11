
repeated_characters = {}

def is_password_good(password):
  found_lower_case = False
  found_upper_case = False
  found_digit = False
  found_special = False
  found_repeated = False

  for c in password:
    if c.islower():
      found_lower_case = True
    elif c.isupper():
      found_upper_case = True
    elif c.isdigit():
      found_digit = True
    elif not c.isalnum():
      found_special = True

    if c in repeated_characters:
      repeated_characters[c] += 1
    else:
      repeated_characters[c] = 1

  for c in password:
    if repeated_characters[c] > 2:
      found_repeated = True

  return len(password) >= 12 and found_lower_case and found_upper_case and found_digit and found_special and not found_repeated

print(is_password_good("AbTp9!fok"))