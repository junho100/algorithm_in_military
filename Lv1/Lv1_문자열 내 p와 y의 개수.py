def solution(s):
    answer = True

    s = s.lower()
    P = s.count("p")
    Y = s.count("y")

    if P != Y:
        return False
    return True

