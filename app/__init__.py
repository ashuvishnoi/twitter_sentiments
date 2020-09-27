from flask_cors import CORS
from flask import Flask, jsonify
import logging
from flask_swagger import swagger
from app.twitter_credibility_controller import twitter_credibility_ratings_handler
from configuration import *
import pickle
import numpy as np
import os
from gensim.models import Word2Vec


# Create a custom logger
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)

# SETUP LOGGING
if not os.path.exists('logs'):
    os.makedirs('logs')


# Create handlers
debug_handler = logging.FileHandler('logs/debug.log')
info_handler = logging.FileHandler('logs/info.log')
debug_handler.setLevel(logging.DEBUG)
info_handler.setLevel(logging.INFO)


# Load tokenizer
with open(TOKENIZER_DISASTER_PATH, 'rb') as tokenizer:
    tk_disaster = pickle.load(tokenizer)

with open(TOKENIZER_HATE_PATH, 'rb') as tokenizer:
    tk_hate = pickle.load(tokenizer)

logging.info('Tokenizers loaded Successfully')

# Load WORD2VEC vectors
model = Word2Vec.load(WORD2VEC_PATH)

logging.info('Word2Vec vectors loaded Successfully')


# Making Emb_Matrix


def make_emb_matrix_disaster():
    word_index = tk_disaster.word_index
    nb_words = len(word_index) + 1
    embedding_matrix = np.zeros((nb_words, EMBEDDING_DIM))
    for word, i in word_index.items():
        if word in model:
            embedding_matrix[i] = model[word]
        elif word.lower() in model:
            embedding_matrix[i] = model[word.lower()]
        elif word[0].upper() + word[1:] in model:
            embedding_matrix[i] = model[word[0].upper() + word[1:]]
    return embedding_matrix


def make_emb_matrix_hate():
    word_index = tk_hate.word_index
    nb_words = len(word_index) + 1
    embedding_matrix = np.zeros((nb_words, EMBEDDING_DIM))
    for word, i in word_index.items():
        if word in model:
            embedding_matrix[i] = model[word]
        elif word.lower() in model:
            embedding_matrix[i] = model[word.lower()]
        elif word[0].upper() + word[1:] in model:
            embedding_matrix[i] = model[word[0].upper() + word[1:]]
    return embedding_matrix


embb_matrix_disaster = make_emb_matrix_disaster()
embb_matrix_hate = make_emb_matrix_hate()
logging.info('Embedding Matrix making Successfully')

tk = (tk_disaster, tk_hate)
embb_matrix = (embb_matrix_disaster, embb_matrix_hate)


twitter_credibility_rating, twitter_disaster_rating, twitter_hate_rating = \
    twitter_credibility_ratings_handler(tk, embb_matrix)


CORS(twitter_credibility_rating)
CORS(twitter_disaster_rating)
CORS(twitter_hate_rating)

# Start the flask server
server = Flask(__name__)
server.register_blueprint(twitter_disaster_rating)
server.register_blueprint(twitter_hate_rating)
server.register_blueprint(twitter_credibility_rating)


@server.route("/", methods=['POST', 'GET'])
def spec():
    return jsonify(swagger(server))
