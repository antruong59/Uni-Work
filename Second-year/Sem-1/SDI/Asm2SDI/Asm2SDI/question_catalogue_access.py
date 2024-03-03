import json
from candidate import Candidate

class QuestionCatalogueAccess:
    def __init__(self, file_path):
        self.__file_path = file_path

    def get_catalogue(self):
        catalogue = []
        with open(self.__file_path) as f:
            data_list = json.load(f)
            for data in data_list:
                candidate = Candidate(data["question"], data["answer"])
                catalogue.append(candidate)
        return catalogue