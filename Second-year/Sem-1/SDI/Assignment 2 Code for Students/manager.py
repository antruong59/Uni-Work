class QuestionAnsweringManager:
    '''Logs and answers asked question'''
    def __init__(self, matching_engine, log_access):
        self.__matching_engine = matching_engine
        self.__log_access = log_access

    def __log_asked_question(self, question):
        self.__log_access.store_asked_question(question)

    def answer_question(self, question_text):
        self.__log_asked_question(question_text)
        return self.__matching_engine.get_matching_question(question_text)
