from Domain.domain_quiz import QuizDomain

class RepoQuiz:
    def __init__(self, file_path):
        self.__list_of_questions = []
        self.__file_path = file_path

    def read_from_file(self):
        """
        reads from the given file the questions
        :return:
        """
        with open(self.__file_path, 'r') as read_file:
            lines = read_file.readlines()
            for line in lines:
                line = line.strip()
                if len(line):
                    quiz_id, text, choice_a, choice_b, choice_c, correct_answ, difficulty = self.split_the_given_input(line)
                    quiz_id = int(quiz_id)
                    self.__list_of_questions.append(QuizDomain(quiz_id, text, choice_a, choice_b, choice_c, correct_answ, difficulty ))

    def add_to_file(self, question):
        """
        appends to the file the newly added question
        :param question:
        :return:
        """
        with open(self.__file_path, 'a') as write_file:
            question_to_write = question.to_file()
            write_file.write(str(question_to_write))

    def init_data(self):
        self.read_from_file()
        return self.__list_of_questions

    def add_question(self, given_input):
        """
        add a question to the list of questions
        :param given_input:
        :return:
        """
        q_id, text, choice_a, choice_b, choice_c, correct_answ, difficulty = self.split_the_given_input(given_input)
        q_id = q_id.split()[1]
        self.check_valid_input(q_id, text, choice_a, choice_b, choice_c, correct_answ, difficulty)
        self.__list_of_questions.append(QuizDomain(q_id, text, choice_a, choice_b, choice_c, correct_answ, difficulty))
        self.add_to_file(QuizDomain(q_id, text, choice_a, choice_b, choice_c, correct_answ, difficulty))

    def check_valid_input(self, q_id, text, choice_a, choice_b, choice_c, correct_answ, difficulty):
        if int(q_id) < 0 and not str(q_id).isnumeric():
            raise ValueError("Invalid id!")
        if str(text).isnumeric():
            raise ValueError("invalid question text!")

    def split_the_given_input(self, given_input):
        given_input = given_input.split(';')
        if len(given_input) != 7:
            raise ValueError("Invalid number of parameters!")
        input_id = given_input[0]
        input_text = given_input[1]
        input_a = given_input[2]
        input_b = given_input[3]
        input_c = given_input[4]
        input_correct = given_input[5]
        input_difficulty = given_input[6]
        return input_id, input_text, input_a, input_b, input_c, input_correct, input_difficulty

    def get_list_of_elements(self):
        list_to_print = ''
        for element in self.__list_of_questions:
            print(element.print_format())
        return list_to_print

    def start_quiz(self, parameters):
        """
        starts a quiz
        :param parameters:
        :return:
        """
        list_current_quiz = []
        first_parameter, second_parameter = self.split_parameters(parameters)
        if second_parameter not in possible_quizes:
            raise ValueError("Given file does not exist!")
        with open(str(second_parameter), 'r') as quiz:
            lines = quiz.readlines()
            for line in lines:
                line = line.strip()
                if len(line):
                    q_id, text, choice_a, choice_b, choice_c, correct_answ, difficulty = self.split_the_given_input(line)
                    q_id = int(q_id)
                    list_current_quiz.append(QuizDomain(q_id, text, choice_a, choice_b, choice_c, correct_answ, difficulty))
        return list_current_quiz

    def playing(self, list, index):
        """
        checks if we are still playing
        :param list:
        :param index:
        :return:
        """
        return index != len(list)

    def keep_playing(self, element_list, index):
        """
        check if we are still playing
        :param element_list:
        :param index:
        :return:
        """
        question_to_print = ''
        for element in element_list:
            if int(element.get_q_id()):
                question_to_print += str(element.get_q_id()) + ' ' + str(element.get_text()) + ' ' + str(element.get_choice_a()) + ' ' + str(element.get_choice_b()) + ' ' + str(element.get_choice_c()) + ' ' + str(element.get_correct_answ()) + ' ' + str(element.get_difficulty())
        return question_to_print

    def check_answer_is_correct(self, answer, index, list_of_elements):
        for elements in list_of_elements:
            if (elements.get_q_id() == index) and elements.get_correct_answ() == answer:
                return True
        return False

    def split_parameters(self, parameters):
        given_param = parameters.split(' ')
        if len(given_param) != 2:
            raise ValueError("Invalid number of parameters to start the quiz!")
        return given_param[0], given_param[1]

possible_quizes = ['questions']