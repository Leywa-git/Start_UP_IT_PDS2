import time
import concurrent.futures


def factorial_calculate(number):
    if number < 2:
        return 1
    else:
        for i in range(1, int(number) + 1):
            number = number * i
    return number


numbers = range(300)

if __name__ == "__main__":
    with concurrent.futures.ThreadPoolExecutor() as executor:
        start_1 = time.time()
        results = executor.map(factorial_calculate, numbers)
        result = list(results)
        print(result)
        end_1 = time.time() - start_1
        result = end_1
        print(result)

if __name__ == "__main__":
    with concurrent.futures.ProcessPoolExecutor() as executor:
        start_2 = time.time()
        results = executor.map(factorial_calculate, numbers)
        result = list(results)
        print(result)
        end_2 = time.time() - start_2
        result = end_2
        print(result)

        print(f"{end_1} - ThreadPoolExecutor, {end_2} - ProcessPoolExecutor")
        if end_1 > end_2:
            print(f"ProcessPoolExecutor took {end_2} seconds and is faster then ThreadPoolExecutor by {end_1 - end_2}")
        else:
            print(f"ThreadPoolExecutor took {end_1} seconds and is faster then ProcessPoolExecutor by {end_2 - end_1}")
