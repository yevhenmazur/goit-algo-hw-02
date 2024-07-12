import re
from collections import deque

def is_palindrome(s: str) -> bool:
    '''Check is the string palindrome or not'''

    # Clear the string
    s = s.lower()
    s = re.sub(r'[^\w\s]', '', s)
    s = re.sub(r'\s+', '', s)

    deq = deque(s)
    while len(deq) > 1:
        if deq.pop() != deq.popleft():
            return False
    return True

STRING = 'Я несу гусеня.' # True
# STRING = 'Я несу каченя.' # False

print(is_palindrome(STRING))
