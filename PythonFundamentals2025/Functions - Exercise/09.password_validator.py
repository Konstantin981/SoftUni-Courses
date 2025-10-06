def check_password(some_password) -> list:
    returned = []
    digits_counter = 0
    if not 6<=len(some_password)<=10:
        returned.append("length")
    for char in some_password:
        if not(ord('a')<=ord(char)<=ord("z") or ord('A')<=ord(char)<=ord('Z') or ord('0')<=ord(char)<=ord('9')):
            returned.append("symbols")
        if ord('0')<=ord(char)<=ord('9'):
            digits_counter+=1
    if digits_counter<2:
        returned.append("digits")
    return returned
password = input()
has_error = False
errors = check_password(password)
if "length" in errors:
    print("Password must be between 6 and 10 characters")
    has_error = True
if "symbols" in errors:
    print("Password must consist only of letters and digits")
    has_error = True
if "digits" in errors:
    print("Password must have at least 2 digits")
    has_error = True
if not has_error:
    print("Password is valid")