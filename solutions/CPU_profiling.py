import cProfile
import pstats
from functools import lru_cache

def fib_naive(n: int) -> int:
    if n < 2:
        return n
    return fib_naive(n - 1) + fib_naive(n - 2)

@lru_cache(maxsize=None)
def fib_cached(n: int) -> int:
    if n < 2:
        return n
    return fib_cached(n - 1) + fib_cached(n - 2)

def run_profile(func, n: int):
    profiler = cProfile.Profile()
    profiler.enable()
    func(n)
    profiler.disable()
    ps = pstats.Stats(profiler).sort_stats('cumtime')
    ps.print_stats(10)

if __name__ == "__main__":
    print("Profiling naive fib(25):")
    run_profile(fib_naive, 25)

    print("\nProfiling cached fib(100):")
    run_profile(fib_cached, 100)

#output= Profiling naive fib(25):
 #        242786 function calls (2 primitive calls) in 0.051 seconds

  # Ordered by: cumulative time

   #ncalls  tottime  percall  cumtime  percall filename:lineno(function)
 #242785/1    0.051    0.000    0.051    0.051 C:/Users/Lenovo/AppData/Local/Programs/Python/Python313/day4.py:6(fib_naive)
  #      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}



#Profiling cached fib(100):
 #        102 function calls (2 primitive calls) in 0.000 seconds

 #  Ordered by: cumulative time

  # ncalls  tottime  percall  cumtime  percall filename:lineno(function)
   # 101/1    0.000    0.000    0.000    0.000 C:/Users/Lenovo/AppData/Local/Programs/Python/Python313/day4.py:11(fib_cached)
    #    1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
