__author__ = 'snowwolf'


def checkio(n, m):
    t = n ^ m
    ret = 0
    while t:
        ret += t & 1
        t >>= 1
    return ret

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(117, 17) == 3, "First example"
    assert checkio(1, 2) == 2, "Second example"
    assert checkio(16, 15) == 5, "Third example"

