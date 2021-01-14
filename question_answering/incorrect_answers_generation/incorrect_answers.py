from .incorrect_answers_fr import *
from .incorrect_answers_en import *


def generate_answers(full_answer, lang="english"):
    """
        Description : Fonction permettant de créer plusieurs réponses (fausses) similaires à partir d'une réponse.
        Arguments :
            - full_answer : Réponse dont on veut le QCM (fausse).
            - lang : Langage de full_answer.
        Returns : (blank_answer, possible_answers)
            - all_answers : Dictionnaire contenant LA bonne réponse et une liste de plusieurs autres réponses fausses.
    """
    if lang == "french":
        all_answers = generate_answers_fr(full_answer)
    elif lang == "english":
        all_answers = generate_answers_en(full_answer)
    return all_answers


if __name__ == "__main__":
    text = "J'irai manger chez vous demain soir."
    incorrect_answers = generate_answers(text)
    print("incorrect_answers : ", incorrect_answers)
