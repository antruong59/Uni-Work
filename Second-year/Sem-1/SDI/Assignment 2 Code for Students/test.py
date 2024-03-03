import pytest
from unittest.mock import Mock
from interactive_console_client import InteractiveConsoleClient
from manager import QuestionAnsweringManager
from access_resources import QuestionCatalogueAccess
from access_resources import QuestionLogAccess
from access_resources import QuestionAnswerPair
from engine import MatchingEngine


@pytest.fixture
def manager():
    '''Get Question Answering manager'''
    question_catalogue_access = QuestionCatalogueAccess('faq.json')
    matching_engine = MatchingEngine(question_catalogue_access)
    question_log_access = QuestionLogAccess('asked_questions_log.txt')
    manager = QuestionAnsweringManager(matching_engine, question_log_access)
    return manager

def test_QuestionCatalogueAccess_get_question_catalogue():
    '''Check the retrived cataloge by order'''
    question_catalogue = QuestionCatalogueAccess('faq.json')
    checkCatalogue = QuestionAnswerPair('What is the weather like today?', 'Same as yesterday.')

    # check catalogue access 
    assert question_catalogue.get_catalogue()[1] == checkCatalogue

def test_QuestionLogAccess_store_asked_question():
    '''Check the latest asked question'''
    log_access = QuestionLogAccess('test_asked_questions_log.txt')
    log_access.store_asked_question('How is the weather?')

    test_log_file = open('test_asked_questions_log.txt')
    all_lines = test_log_file.readlines()
    test_log_file.close()

    # check question logging
    assert all_lines[-1] == 'How is the weather?\n'

def test_MatchingEngine_get_matching_question():
    '''Check matching question and matching score'''
    catalogue_access = QuestionCatalogueAccess('faq.json')
    matching_engine = MatchingEngine(catalogue_access)
    candidate_object, match_score = matching_engine.get_matching_question('How is the weather?')
    test_question_template = QuestionAnswerPair('What is the weather like today?', 'Same as yesterday.')

    # check template question and matching score
    assert candidate_object == test_question_template
    assert match_score == 3/7

def test_QuestionAnsweringManager(manager):
    '''Check manager retrieving data'''
    candidate_object, score = manager.answer_question('How is the weather?')
    test_question_template = QuestionAnswerPair('What is the weather like today?', 'Same as yesterday.')
    test_log_file = open('asked_questions_log.txt')
    all_lines = test_log_file.readlines()
    test_log_file.close()

    # check template question and matching score
    assert candidate_object == test_question_template
    assert score == 3/7

    # check question logging
    assert all_lines[-1] == 'How is the weather?\n'

def test_manager_calls_matching_engine_and_log_access():
    '''Check manager calling classes and corresponding functions'''
    matching_engine = Mock()
    log_access = Mock()
    manager = QuestionAnsweringManager(matching_engine, log_access)
    manager.answer_question('What is your name?')

    # check manager functions calling 
    assert matching_engine.get_matching_question.called_once_with('What is your name?')
    assert log_access.store_asked_question.called_once_with('What is your name?')
