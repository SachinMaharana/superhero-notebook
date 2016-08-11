import random
import string
import caching

def random_string(length):
    s = ''
    for i in range(length):
        s = s + random.choice(string.ascii_letters)
    return s

caching.init()

for n in range(1000):
    while True:
        key = random_string(20)
        if caching.contains(key):
            continue
        else:
            break
    value = random_string(20)
    caching.set(key, value)
    print("After {} iterations, cache has {} entries".format(n+1, caching.size()))
