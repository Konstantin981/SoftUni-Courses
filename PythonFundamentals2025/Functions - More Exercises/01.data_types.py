def data(data_type, value):
    if data_type == "int":
        value = int(value)
        return value*2
    elif data_type == "real":
        value = float(value)
        value = value * 1.5
        return f"{value:.2f}"
    else:
        value = f"${value}$"
        return value
command = input()
number_or_string = input()
result = data(command, number_or_string)
print(result)