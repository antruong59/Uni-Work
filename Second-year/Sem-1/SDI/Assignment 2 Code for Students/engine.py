import utils as u

class MatchingEngine:
    '''Computes the most similar question-answer pair for a given question text'''
    def __init__(self, catalogue_access):
        self.__question_catalogue_access = catalogue_access

    def get_matching_question(self, question):
        words = u.text_to_words(question)
        lowercase_words = u.words_to_lowercase(words)

        max_score = 0
        question_answer_pairs = self.__question_catalogue_access.get_question_catalogue()

        for pair in question_answer_pairs:
            template_question = pair.question
            template_words = u.text_to_words(template_question)
            template_lowercase_words = u.words_to_lowercase(template_words)
            
            # calculate match score
            match_score = u.jaccard_similarity_score(lowercase_words, template_lowercase_words)

            if match_score > max_score:
                max_score = match_score
                match_question = pair
            else:
                match_question = False # return candidate = False for no matched questions

        return match_question, max_score


