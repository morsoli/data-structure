from pythonds.basic.deque import Deque

def check(test_str):
    char_deque = Deque()

    for ch in test_str:
        char_deque.addFront(ch)
    still_equal = True
    while still_equal and char_deque.size()>1:
        first = char_deque.removeFront()
        end = char_deque.removeRear()
        if first!=end:
            still_equal=False
        return still_equal
print(check("asdsa"))
print(check("asdad"))