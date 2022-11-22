import time
import concurrent.futures


def factorial_calculate(number):
    if number < 2:
        return 1
    else:
        for i in range(1, int(number) + 1):
            number = number * i
    return number


numbers_1 = range(80)
numbers_2 = range(70)

if __name__ == "__main__":
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        start_1 = time.time()
        task_1 = executor.map(factorial_calculate, numbers_1)
        task_2 = executor.map(factorial_calculate, numbers_2)
        result = list(task_1) + list(task_2)
        print(result)
        end_1 = time.time() - start_1
        print(end_1)

    with concurrent.futures.ProcessPoolExecutor(max_workers=10) as executor:
        start_2 = time.time()
        task_1 = executor.map(factorial_calculate, numbers_1)
        task_2 = executor.map(factorial_calculate, numbers_2)
        result = list(task_1) + list(task_2)
        print(result)
        end_2 = time.time() - start_2
        print(end_2)

        print(f"{end_1} - ThreadPoolExecutor, {end_2} - ProcessPoolExecutor")
        if end_1 > end_2:
            print(f"ProcessPoolExecutor took {end_2} seconds and is faster then ThreadPoolExecutor by {end_1 - end_2}")
        else:
            print(f"ThreadPoolExecutor took {end_1} seconds and is faster then ProcessPoolExecutor by {end_2 - end_1}")
