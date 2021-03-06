from writer import Writer
import os

# This is the interface for the Writer class
# to init this class you need to pass nothing to constructor

class WriterInterface(Writer):

    word_file = "word.txt"

    validate_file = "validate.txt"

    letters_file = "letters.txt"

    def save_word(self, word):
        hidden_word = self.hide_letters(word)

        self.write_txt(self.word_file, hidden_word)
        self.write_txt(self.validate_file, word)

    def return_word(self):
        content = self.read_txt(self.word_file)
        content = list(content)

        result = []
        for index, item in enumerate(content):
            result.append(item)
            if index < len(content) - 1:
                result.append(",")

        return "".join(result)

    def return_full_word(self):
        return self.read_txt(self.word_file)

    def guess_letter(self, value):
        validator = self.read_txt(self.validate_file)
        validator_letters = list(validator)

        word = self.read_txt(self.word_file)
        word_letters = list(word)

        result = False
        for index, item in enumerate(validator_letters):
            if item == value:
                word_letters[index] = value
                result = True

        self.write_txt(self.word_file, "".join(word_letters))
        if result == False:
            file_path = "{}/{}".format(self.folder,self.letters_file)
            if os.stat(file_path).st_size == 0:
                self.append_txt(self.letters_file, value)
            else:
                self.append_txt(self.letters_file, "-" + value)

        return result

    def is_winner(self):
        word = self.read_txt(self.word_file)
        if word.find("_") > 0:
            return False
        elif word.find("_") < 0:
            self.reset_file(self.letters_file)
            return True

    def game_over(self):
        self.reset_file(self.letters_file)

    def failed_letters(self):
        return self.read_txt(self.letters_file)
