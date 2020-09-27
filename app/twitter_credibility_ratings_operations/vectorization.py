from keras.preprocessing.sequence import pad_sequences
import pandas as pd
from configuration import maxlen
import logging
import numpy as np


def convert_into_vectors_disaster(text, tk_disaster, embedding_matrix):
    '''
    :param text: List of strings
    :param tk_disaster: tokenizer
    :return: List of padded vectors
    '''
    logging.debug('Vectorization of text Started')
    x_tokenized = tk_disaster.texts_to_sequences(pd.Series(text).fillna('UNK'))
    padded_seq = pad_sequences(x_tokenized, maxlen=maxlen, padding='post', truncating='post')
    emb_data = [embedding_matrix[[i]] for i in padded_seq]
    emb_data = np.array(emb_data)
    return emb_data


def convert_into_vectors_hate(text, tk_hate, embedding_matrix):
    '''
    :param text: List of strings
    :param tk_hate: tokenizer
    :return: List of padded vectors
    '''
    logging.debug('Vectorization of text Started')
    x_tokenized = tk_hate.texts_to_sequences(pd.Series(text).fillna('UNK'))
    padded_seq = pad_sequences(x_tokenized, maxlen=maxlen, padding='post', truncating='post')
    emb_data = [embedding_matrix[[i]] for i in padded_seq]
    emb_data = np.array(emb_data)
    return emb_data
