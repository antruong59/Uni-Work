import json as js
from dataclasses import dataclass

class QuestionCatalogueAccess:
    '''Retrieves questions from the question catalogue store'''
    def __init__(self, file_name_path):
        self.__file_name_path = file_name_path

    def get_question_catalogue(self):
        question_catalogue = []
        with open(self.__file_name_path) as file:
            data_set = js.load(file)
            for data in data_set:
                question_answer_pair = QuestionAnswerPair(data['question'], data['answer'])
                question_catalogue.append(question_answer_pair)
        return question_catalogue

class QuestionLogAccess:
    '''Stores the asked questions in the Asked Questions Store'''
    def __init__(self, file_name_path):
        self.__file_name_path = file_name_path

    def store_asked_question(self, question):
        asked_question_store_file = open(self.__file_name_path, 'a+')
        asked_question_store_file.write(f'{question}\n')
        asked_question_store_file.close()

@dataclass
class QuestionAnswerPair:
    question : str
    answer : str