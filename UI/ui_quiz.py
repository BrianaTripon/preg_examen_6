class UI:
    def __init__(self, controller):
        self.__controller = controller

    @staticmethod
    def print_menu():
        print("Add a new question.")
        print("Start a quiz. (questions)")
        print("Exit.")

    def start(self):
        self.__controller.init_list()
        self.print_menu()
        while True:
            try:
                user_input = input("Enter your option: ")
                if len(user_input) < 1:
                    raise ValueError("Invalid option!")
                if self.split_parameters(user_input).lower() == 'add':
                    self.__controller.add_new_question(user_input)
                    print("Question added successfully!")
                elif self.split_parameters(user_input).lower() == 'exit':
                    return
                elif self.split_parameters(user_input).lower() == 'start':
                    list_of_questions = self.__controller.start_quiz(user_input)
                    are_we_still_playing = True
                    index = 1
                    while are_we_still_playing:
                        try:
                            are_we_still_playing = self.__controller.are_we_playing(list_of_questions, index)
                            current_question = self.__controller.keep_playing(list_of_questions, index)
                            print(current_question)
                            user_choice = input("Enter your choice: ")
                            answer = self.__controller.check_correct_answer(user_choice, index, list_of_questions)
                            index += 1
                            print(answer)
                        except ValueError as ve:
                            print(str(ve))
            except ValueError as ve:
                print(str(ve))

    def split_parameters(self, user_option):
        user_option = user_option.split()
        return user_option[0]