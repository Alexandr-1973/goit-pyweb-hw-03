from math import isqrt
import time
from multiprocessing import Pool, cpu_count

def get_factors(number):
    factors = set()
    for i in range(1, isqrt(number) + 1):
        if number % i == 0:
            factors.add(i)
            factors.add(number // i)
    return sorted(factors)

def sync_factorize(*numbers):
    start_time = time.perf_counter()
    need_list = [get_factors(number) for number in numbers]
    end_time = time.perf_counter()
    print(f"Synchronous execution time: {end_time - start_time:.4f} seconds")
    return need_list

def multi_factorize(*numbers):
    with Pool(processes=cpu_count()) as pool:
            multi_start_time = time.perf_counter()
            need_list = pool.map(get_factors, numbers)
            multi_end_time = time.perf_counter()
            print(f"Multiprocessing execution time: {multi_end_time - multi_start_time:.4f} seconds")
    return need_list

if __name__ == '__main__':

    a, b, c, d = sync_factorize(128, 255, 99999, 10651060)
    ma, mb, mc, md = multi_factorize(128, 255, 99999, 10651060)
    print(f"Synchronous values tests:\na = {a}\nb = {b}\nc = {c}\nd = {d}")
    print(f"Multiprocessing values tests:\na = {ma}\nb = {mb}\nc = {mc}\nd = {md}")

    numbers = [10651060080, 106510600080, 1065106000080, 10651060000080, 106510600000087, 1065106000000008, 10651060000000008, 1065106000000008,
               10651060080, 106510600080, 1065106000080, 10651060000080, 106510600000087, 1065106000000008, 10651060000000008, 1065106000000008,
               10651060080, 106510600080, 1065106000080, 10651060000080, 106510600000087, 1065106000000008, 10651060000000008, 1065106000000008,
               10651060080, 106510600080, 1065106000080, 10651060000080, 106510600000087, 1065106000000008, 10651060000000008, 1065106000000008]

    sync_factorize(*numbers)
    multi_factorize(*numbers)
