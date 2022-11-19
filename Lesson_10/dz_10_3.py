# Створюємо користувацький клас виключення
class CorrectAgeError(Exception):

    # Створюється конструктор та виконується метод __init__ ініциалізуються атрибути
    def __init__(self, *args):
        # Створюється умова на перевірку, чи передається значення атрибуту та прописуються додаткові атрибути
        if args:
            self.age = args[0]
        else:
            self.age = None
        self.min_age = 1
        self.max_age = 150

    # Змінюємо метод __str__, що повертає нам рядок
    def __str__(self):
        # Задаємо умови перевірки переданого значення з прописаними та повертаємо користувацький рядок відповідно
        if self.age < self.min_age:
            return f"Age {self.age} is impossible. You are not born yet if younger then {self.min_age}"
        elif self.age > self.max_age:
            return f"Age {self.age} is impossible. You are probably dead already if older then {self.max_age}"
        else:
            return "CorrectAgeError raised"


# Створюємо змінну та присвоюємо їй інтове значення. Значення можна замінити на 0
number = 158
# Задаємо умову для виклику виключення
if not 1 <= number <= 150:
    # Викликаємо користувацьке виключення та передаємо йому значення створеної змінної
    raise CorrectAgeError(number)
