page_amount=int(input())
pages_per_hour=int(input())
days=int(input())
time = page_amount // pages_per_hour
result = time // days
print(result)