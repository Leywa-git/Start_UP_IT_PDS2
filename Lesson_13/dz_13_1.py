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

print(int_list)
print(float_list)
print(str_list)
