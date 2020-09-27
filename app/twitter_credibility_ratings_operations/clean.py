import re
import logging


def clean_text(text):
    text = str(text)
    """
    Function to clean the given text
    :param text: Sentence string
    :return: Cleaned sentence string
    """

    lower = False
    text = re.sub(r"(?:\@|https?\://)\S+", "", text)
    for punct in "/-'":
        text = text.replace(punct, ' ')
    for punct in '&':
        text = text.replace(punct, f' {punct} ')
    for punct in '.!?,#$%\()*+-/:;=""[\\]^_`{|}~':
        text = text.replace(punct, '')
    if lower:
        text = text.lower()
    text = re.sub('\d+\d+', 'NUM', text)
    return text


def cleaning_of_texts(texts):
    logging.debug('Cleaning of text Started')
    return [clean_text(text) for text in texts]
