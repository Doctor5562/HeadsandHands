import random

MAX_NUM = 1_0

def generator(n):
    result = {}
    
    for i in range(n):
        size = random.randint(0, MAX_NUM)
        while size in result:
            size = random.randint(0, MAX_NUM)
        array = [random.randint(-MAX_NUM, MAX_NUM) for _ in range(size)]
        array.sort(reverse=i%2)
        result[size] = array
    return list(result.values())

print(generator(5))
