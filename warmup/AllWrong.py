# Write any import statements here

def getWrongAnswers(N: int, C: str) -> str:
    return choseWrong(C)


def choseWrong(answers):
    wrongAnswers = ''
    for answer in answers:
        if answer == 'A':
            wrongAnswers += 'B'
        else:
            wrongAnswers += 'A'
    return wrongAnswers
