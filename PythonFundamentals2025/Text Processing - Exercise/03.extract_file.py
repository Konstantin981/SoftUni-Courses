file_adress = input().split("\\")
file, extension = file_adress[len(file_adress)-1].split(".")
print(f"File name: {file}")
print(f"File extension: {extension}")