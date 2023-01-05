import time
import random
from random_words import RandomWords

int_list = []
float_list = []
str_list = []

words = RandomWords()

for i in range(0, 5000):
    int_list.append(random.randint(0, 1000))
    float_list.append(random.uniform(0.1, 100.0))
    str_list.append(words.random_word())


def insertion_sort(data):
    for scanIndex in range(1, len(data)):
        tmp = data[scanIndex]
        minIndex = scanIndex
        while minIndex > 0 and tmp < data[minIndex - 1]:
            data[minIndex] = data[minIndex - 1]
            minIndex -= 1
        data[minIndex] = tmp


def average_sort_time(list_name, cycle_quantity):
    counter = cycle_quantity
    cycles = []
    end_time = 0
    while counter != 0:
        start_time = time.time()
        insertion_sort(list_name)
        end_time += time.time() - start_time
        cycles.append(end_time)
        counter -= 1
    print(cycles)
    average = sum(cycles) / len(cycles)
    return print(f"Average sort time for {cycle_quantity} insertion sort cycles: {average}")


average_sort_time(int_list, 10)
