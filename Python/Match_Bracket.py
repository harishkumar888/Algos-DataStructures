# Displays the number of brackets need to match all brackets.abs

from collections import deque

def bracket_match(bracket_string):
  br_stack = deque()
  closing_br = 0
  for br in bracket_string:
    if br == '(':
      br_stack.append(br)
    elif br == ')':
      if not br_stack:
        closing_br += 1
        continue
      br_stack.pop()
  return len(br_stack)+closing_br

print(bracket_match("(((()"))
