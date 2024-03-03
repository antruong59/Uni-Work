from interactive_console_client import InteractiveConsoleClient
from question_answering_manager import QuestionAnsweringManager
from question_catalogue_access import QuestionCatalogueAccess
from question_log_access import QuestionLogAccess
from matching_engine import MatchingEngine

def main(candidates_path, questions_log_path):
    catalogue_access = QuestionCatalogueAccess(candidates_path)
    engine = MatchingEngine(catalogue_access)
    log_access = QuestionLogAccess(questions_log_path)
    manager = QuestionAnsweringManager(engine, log_access)
    #
    client = InteractiveConsoleClient(manager)
    client.run()


if __name__ == '__main__':
    main("faq.json", "asked_questions_log.txt")
