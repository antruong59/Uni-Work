from interactive_console_client import InteractiveConsoleClient
import pytest
from unittest.mock import Mock
import mock
from question_answering_manager import QuestionAnsweringManager
from question_catalogue_access import QuestionCatalogueAccess
from question_log_access import QuestionLogAccess
from matching_engine import MatchingEngine
from candidate import Candidate


@pytest.fixture
def manager():
    catalogue_access = QuestionCatalogueAccess("faq.json")
    match_engine = MatchingEngine(catalogue_access)
    log_access = QuestionLogAccess("asked_questions_log.txt")
    manager = QuestionAnsweringManager(match_engine, log_access)
    return manager

def test_question_catalogue_access_get_catalogue_list():
    catalogue = QuestionCatalogueAccess("faq.json")
    firstCatalogue = Candidate("What day is today?", "Monday")
    assert catalogue.get_catalogue()[0] == firstCatalogue

def test_question_log_access_store_question():
    log_access = QuestionLogAccess("test_asked_questions_log.txt")
    log_access.store_asked_question("What is your name?")

    test_log_file = open("test_asked_questions_log.txt", "r")
    line_list = test_log_file.readlines() # get all the lines in test file
    test_log_file.close()

    # check if the last line of the file is the asked question
    assert line_list[len(line_list) - 1] == "What is your name?\n"

def test_matching_engine_match_question():
    catalogue_access = QuestionCatalogueAccess("faq.json")
    match_engine = MatchingEngine(catalogue_access)
    candidate, score = match_engine.match_question("How is the weather?")
    test_candidate = Candidate("What is the weather like today?", "Same as yesterday.")
    assert candidate == test_candidate
    assert score == 3/7

def test_manager_calls_engine_and_accessor():
    match_engine = Mock()
    log_accessor = Mock()
    manager = QuestionAnsweringManager(match_engine, log_accessor)
    manager.answer_question("What is it?")

    assert match_engine.match_question.called_once_with("What is it?")
    assert log_accessor.store_asked_question.called_once_with("What is it?")

def test_question_answering_manager(manager):
    candidate, score = manager.answer_question("How is the weather?")
    test_candidate = Candidate("What is the weather like today?", "Same as yesterday.")
    test_log_file = open("asked_questions_log.txt", "r")
    line_list = test_log_file.readlines()
    test_log_file.close()

    # test results of answer_question function
    assert candidate == test_candidate
    assert score == 3/7

    # test store asked question function
    assert line_list[len(line_list) - 1] == "How is the weather?\n"

def test_console_client_read_question_input(manager):
    client = InteractiveConsoleClient(manager)

    with mock.patch('builtins.input', return_value="What is it?"):
        assert client._read_question() == "What is it?"
        assert client._read_and_answer_question() == True