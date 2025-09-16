import tracemalloc
import time
def leak(n: int):
    leaked = []
    for i in range(n):
        leaked.append('x' * 10000)
    return leaked

if __name__ == "__main__":
    tracemalloc.start()
    snap1 = tracemalloc.take_snapshot()
    leaked = leak(1000)
    snap2 = tracemalloc.take_snapshot()
    top_stats = snap2.compare_to(snap1, 'lineno')

    print("Top memory differences (snap2 vs snap1):")
    for stat in top_stats[:10]:
        print(stat)
    print("Leaked objects stored in `leaked` list (len):", len(leaked))
    time.sleep(1)



# output: Top memory differences (snap2 vs snap1):
# C:/Users/Lenovo/AppData/Local/Programs/Python/Python313/day4.py:9: size=9814 KiB (+9814 KiB), count=1001 (+1001), average=10040 B
# C:\Users\Lenovo\AppData\Local\Programs\Python\Python313\Lib\tracemalloc.py:560: size=328 B (+328 B), count=1 (+1), average=328 B
# C:\Users\Lenovo\AppData\Local\Programs\Python\Python313\Lib\tracemalloc.py:423: size=328 B (+328 B), count=1 (+1), average=328 B
# Leaked objects stored in `leaked` list (len): 1000
