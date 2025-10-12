lst = input().split()
palindrome = input()
palindrome_lst = [word for word in lst if word==word[::-1]]
count = lst.count(palindrome)
print(palindrome_lst)
print(f"Found palindrome {count} times")