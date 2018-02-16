from collections import deque

word = "toioot"

my_deque = deque(word)

def check_pali(new_deque):
  for i in range(int(len(new_deque)/2)):
    if new_deque.pop() is not new_deque.popleft():
      return False
  return True

print(check_pali(my_deque))

