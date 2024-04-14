"""All Wrong"""

def get_wrong_answers(n: int, c: str) -> str:
    """
    Returns a string with N characters,
    where the ith character is the answer to give for question i to get it wrong.

    Args:
        n (int): The number of questions.
        c (str): The correct answer string containing 'A' or 'B' for each question.

    Returns:
        str: A string with N characters representing the wrong answers to give.
    """
    word = list(c)
    for index in range(n):
        if word[index] == 'A':
            word[index] = 'B'
        else: word[index] = 'A'
    return "".join(word)

get_wrong_answers(3, 'ABA')
get_wrong_answers(5, 'BBBBB')
