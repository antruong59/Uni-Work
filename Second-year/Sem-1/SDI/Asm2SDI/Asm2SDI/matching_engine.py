import utils

class MatchingEngine:
    def __init__(self, catalogue_access):
        self.__catalogue_access = catalogue_access

    def match_question(self, question):
        words = utils.text_to_words(question)
        lower_case_words = utils.words_to_lowercase(words)
        max_score = 0
        for candidate in self.__catalogue_access.get_catalogue():
            candidate_question = candidate.question
            candidate_words = utils.words_to_lowercase(utils.text_to_words(candidate_question))
            score = utils.jaccard_similarity_score(lower_case_words, candidate_words)
            if score >= max_score:
                max_score = score
                match_candidate = candidate

        return (match_candidate, max_score)