class ControllerQuiz:
    def __init__(self, repo):
        self.__repo = repo

    def add_new_question(self, question):
        return self.__repo.add_question(question)

    def init_list(self):
        return self.__repo.init_data()

    def fet_list(self):
        return self.__repo.get_list_of_elements()

    def start_quiz(self, quiz):
        return self.__repo.start_quiz(quiz)

    def are_we_playing(self, list_of_elem, index):
        return self.__repo.playing(list_of_elem, index)

    def keep_playing(self, list, current_index):
        return self.__repo.keep_playing(list, current_index)

    def check_correct_answer(self, answer, index, list_of_elements):
        return self.__repo.check_answer_is_correct(answer, index, list_of_elements)

