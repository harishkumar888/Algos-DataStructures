from collections import deque

word = "toioot"

my_deque = deque(word)

def is_palindrome(new_deque):
  for i in range(int(len(new_deque)/2)):
    if new_deque.pop() is not new_deque.popleft():
      return False
  return True

print(is_palindrome(my_deque))

