import sys
import time

my_list_1 = [1, 2, 3, 4, 0, 7]
my_list_2 = [1, 3, 5, 7.8, 9]
my_list_3 = [1, 2, 5, "a", 10]
my_list_4 = [1, 2, 1, 7, 8, 10]


def list_checker(lists):
    try:
        for i in lists:
            a = i/1
            if isinstance(i, float):
                i.replace(".", "", 1).isdigit()
            else:
                pass
        if len(lists) == len(set(lists)):
            print(lists, "- all elements in the list are unique")
        else:
            print(lists, "- there are duplicated elements in the list")
    except TypeError:
        print(lists, "- list contains a character or word! Replace it with a whole number!", file=sys.stderr)
    except AttributeError:
        print(lists, "- list contains a float number! Replace it with a whole number!", file=sys.stderr)
    except Exception as ex:
        print(ex, "I didn't predicted this. Sorry!")


list_checker(my_list_1)
time.sleep(0.01)            # Бібліотека time та функція sleep використані для зручнішого відображення та порівняння
list_checker(my_list_2)
time.sleep(0.01)
list_checker(my_list_3)
time.sleep(0.01)
list_checker(my_list_4)
