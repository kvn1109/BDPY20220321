import time
from multiprocessing import Pool

COUNT = 100000000
SPLIT = 4


def countdown(n):
    global COUNT
    for i in range(n):
        COUNT -= 1

#what' s diffrent pool & process
if __name__ == '__main__':
    pool = Pool(processes=SPLIT)

    start = time.time()
    for _ in range(SPLIT):
        print("start a pool async")
        p = pool.apply_async(countdown, [COUNT // SPLIT])
    pool.close()
    pool.join()
    end = time.time()
    print('Time taken in seconds ->', end - start)
