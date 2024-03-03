class QuestionAnsweringManager:
    def __init__(self, match_engine, log):
        self.__match_engine = match_engine
        self.__log = log
    
    # answer and log asked the question
    def answer_question(self, question):
        self.__store_asked_question(question)
        return self.__match_engine.match_question(question)

    def __store_asked_question(self, question_text):
        self.__log.store_asked_question(question_text)

