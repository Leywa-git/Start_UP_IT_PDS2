"""
Программа буде запитувати ціле число від юзера, доки юзер не введе ціле число від 1 до 12
Введіть число з плавоючою крапкою для виклику ValueError
Введіть букву, або слово для виклику TypeError
"""
import sys
import time


def month_number():

    months = {12: "December", 1: "January", 2: "February",
              3: "March", 4: "April", 5: "May",
              6: "June", 7: "July", 8: "August",
              9: "September", 10: "October", 11: "November"}
    month = input("Enter the month number:")

    try:
        result = ""
        number = month.replace(" ", "")

        if number.replace(".", "", 1).isdigit():
            number = int(number)
        else:
            pass

        if number >= 13 or number < 1:
            print("There is no month with such number!")
            month_number()
        else:
            for k, v in months.items():
                if number == k:
                    result += v
        return print(result)

    except ValueError as ex:
        print("You entered a number with digit, enter the month number!", file=sys.stderr)
        print(ex)
        time.sleep(0.1)     # Бібліотека time та функція sleep використані для гарнішого відображення
        month_number()
    except TypeError as ex:
        print("You entered a word or an alphabetical character, enter the month number!", file=sys.stderr)
        print(ex)
        time.sleep(0.1)
        month_number()
    except Exception as ex:
        print("Unexpected Error occurred, please, contact our support", file=sys.stderr)
        print(ex)


month_number()
