
def solution(A):
    # write your code in Python 3.6
    a = set(A)
    ans = 1
    while ans in a:
       ans += 1
    return ans
