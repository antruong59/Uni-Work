class QuestionLogAccess:
    def __init__(self, file_path):
        self.__file_path = file_path
        
    def store_asked_question(self, question):
        file = open(self.__file_path, "a+")
        file.write(f'{question}\n')
        file.close()