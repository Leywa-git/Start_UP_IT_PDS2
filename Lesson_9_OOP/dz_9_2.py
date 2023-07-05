class TextProcessor:
    def __init__(self):
        self.punctuation = "'.,!?;:*()-[]{}/"

    def __is_punctuation(self, sign):
        return sign in self.punctuation

    def get_clean_string(self, text):
        clean_text = ""
        for sign in text:
            if self.__is_punctuation(sign):
                continue
            clean_text += sign
        return clean_text


class TextLoader:
    def __init__(self):
        self.__text_processor = TextProcessor()
        self.__clean_string = ""

    def set_clean_text(self, text):
        self.__clean_string = self.__text_processor.get_clean_string(text)

    @property
    def clean_string(self):
        print("Cleaned text is shown:")
        return self.__clean_string


class DataInterface:
    def __init__(self):
        self.__text_loader = TextLoader()

    def process_texts(self, text):
        self.__text_loader.set_clean_text(text)
        split_text = self.__text_loader.clean_string.split("\n")
        for i in split_text:
            return i


cleaner = DataInterface()
my_text = """I, a fresh (beginner) IT guy, am curious! How to make a list - {} or []? \
          Today, tomorrow or later - only matter of a time! \
          / - is this a right symbol?"""
print(cleaner.process_texts(my_text))
