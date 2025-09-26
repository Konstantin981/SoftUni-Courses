lines = int(input())
last_bracket = ''
first_bracket = ''
total_open = 0
total_closed = 0
balanced = True
for _ in range(lines):
    line = input()
    if line == '(':
        if last_bracket == '(':
            balanced = False
        last_bracket = "("
        total_open += 1
        if first_bracket == '':
            first_bracket = '('
    if line == ')':
        if last_bracket == ')':
            balanced = False
        last_bracket = ")"
        total_closed += 1
        if first_bracket == '':
            first_bracket = ')'
            balanced = False

if total_open != total_closed:
    balanced = False
if balanced:
    print("BALANCED")
else:
    print("UNBALANCED")