version = input().split(".")
if version[2] != "9":
    integer_num = int(version[2]) + 1
    version[2] = str(integer_num)
else:
    if version[1] != "9":
        integer_num = int(version[1]) + 1
        version[1] = str(integer_num)
        version[2] = "0"
    else:
        integer_num = int(version[0]) + 1
        version[0] = str(integer_num)
        version[2] = "0"
        version[1] = "0"
print (".".join(version))