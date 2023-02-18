class QuizDomain:
    def __init__(self, q_id, text, choice_a, choice_b, choice_c, correct_answ, difficulty):
        self.__q_id = q_id
        self.__text = text
        self.__choice_a = choice_a
        self.__choice_b = choice_b
        self.__choice_c = choice_c
        self._correct_answ = correct_answ
        self.__difficulty = difficulty

    def get_q_id(self):
        return self.__q_id

    def get_text(self):
        return self.__text

    def get_choice_a(self):
        return self.__choice_a

    def get_choice_b(self):
        return self.__choice_b

    def get_choice_c(self):
        return self.__choice_c

    def get_correct_answ(self):
        return self._correct_answ

    def get_difficulty(self):
        return self.__difficulty

    def print_format(self):
        return str(str(self.__q_id) + ' ' + str(self.__text) + ' ' + str(self.__choice_a) + ' ' + str(self.__choice_b) + ' ' + str(self.__choice_c) + ' ' + str(self._correct_answ) + ' ' + str(self.__difficulty))

    def from_file(self, given_input):
        given_input = given_input.split(';')
        input_id = given_input[0]
        input_text = given_input[1]
        input_a = given_input[2]
        input_b = given_input[3]
        input_c = given_input[4]
        input_correct = given_input[5]
        input_difficulty = given_input[6]
        return input_id, input_text, input_a, input_b, input_c, input_correct, input_difficulty

    def to_file(self):
        return '\n' + str(str(self.__q_id) + ';' + str(self.__text) + ';' + str(self.__choice_a) + ';' + str(self.__choice_b) + ';' + str(self.__choice_c) + ';' + str(self._correct_answ) + ';' + str(self.__difficulty))
