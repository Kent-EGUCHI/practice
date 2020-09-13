import time

num = 100
diff = 0

def scheduler(agr1, arg2):
    t1 =time.monotonic()
    diff = t1-t0
    print(t1)


for _ in range(num):
    t0 = time.perf_counter()
    #time.sleep(0)
    pass
    t1 = time.perf_counter()
    diff = t1 - t0
    print(diff)