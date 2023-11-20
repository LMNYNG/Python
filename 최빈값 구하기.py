def solution(array):
    freq=[array.count(i) for i in set(array)]
    m=max(freq)
    return -1 if freq.count(m)>1 else list(set(array))[freq.index(m)]
