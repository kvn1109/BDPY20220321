import time
from threading import Thread

COUNT = 100000000


def countdown(n):
    global COUNT
    for i in range(n):
        COUNT -= 1


SPLIT = 4
threads = []
for _ in range(SPLIT):
    print(f"generate a thread with argument:{COUNT // SPLIT}")
    t = Thread(target=countdown, args=(COUNT // SPLIT,))
    threads.append(t)

start = time.time()
for t in threads:
    print("start a thread")
    t.start()
for t in threads:
    t.join()
# countdown(COUNT)
end = time.time()

print('Time taken in seconds ->', end - start)