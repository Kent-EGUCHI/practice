import time

num = 100
diff = 0

for _ in range(num):
    t0 = time.perf_counter()
    time.sleep(0.001)
    t1 = time.perf_counter()
    diff = t1 - t0
    print(diff)