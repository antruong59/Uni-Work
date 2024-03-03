from interactive_console_client import InteractiveConsoleClient
from manager import QuestionAnsweringManager
from access_resources import QuestionCatalogueAccess
from access_resources import QuestionLogAccess
from engine import MatchingEngine

def main(candidates_path, questions_log_path):
    #TODO your initialization code goes here, replacing the `manager = None` statement
    #
    question_catalogue_access = QuestionCatalogueAccess(candidates_path)
    matching_engine = MatchingEngine(question_catalogue_access)
    question_log_access = QuestionLogAccess(questions_log_path)
    manager = QuestionAnsweringManager(matching_engine, question_log_access)
    #
    client = InteractiveConsoleClient(manager)
    client.run()


if __name__ == '__main__':
    main("faq.json", "asked_questions_log.txt")
