from Controller.controller_quiz import ControllerQuiz
from Repository.repository_quiz import RepoQuiz
from UI.ui_quiz import UI

repo = RepoQuiz('questions')
controller = ControllerQuiz(repo)
ui = UI(controller)
ui.start()
