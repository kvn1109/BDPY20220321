import time
from multiprocessing import Process

COUNT = 100000000
SPLIT = 4


def countdown(n):
    global COUNT
    for i in range(n):
        COUNT -= 1


if __name__ == '__main__':
    start = time.time()
    processes = []
    for _ in range(SPLIT):
        print(f"generate a process with args={COUNT // SPLIT}")
        p = Process(target=countdown, args=(COUNT // SPLIT,))
        processes.append(p)
    for p in processes:
        print("start a process")
        p.start()
    for p in processes:
        p.join()
    end = time.time()

    print('Time taken in seconds ->', end - start)