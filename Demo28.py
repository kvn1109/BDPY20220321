import time

COUNT = 100000000


def countdown(n):
    global COUNT
    for i in range(n):
        COUNT -= 1


start = time.time()
countdown(COUNT)
end = time.time()

print('Time taken in seconds ->', end - start)