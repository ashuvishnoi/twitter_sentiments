from app.twitter_credibility_ratings_operations.model import lstm_model
import logging
import tensorflow as tf
import keras
from configuration import *


def predict(vectors, feature_type):

    '''
       Fn to predict the credibility scores and labels
       :param vectors: vectors
       :param feature_type: hate or clickbait like strings
       :return: list of predictions obj
       '''

    if feature_type == 'disaster':
        logging.debug(f"{feature_type} score predictions started")
        model = lstm_model()

        graph = tf.get_default_graph()
        with graph.as_default():
            model.load_weights(MODEL_PATH_DISASTER)
            y_pred = model.predict(vectors)
        y_pred_2 = (y_pred > DISASTER_THRESHOLD) + 0
        predictions = ['Disaster' if i == 1 else 'Non Disaster' for i in y_pred_2]
        keras.backend.clear_session()
        preds = [float(i) for i in y_pred]
        res = [{'Label': label, 'Score': score} for label, score in zip(predictions, preds)]
        logging.debug(f"{feature_type} score predictions Successfully")
        return res

    elif feature_type == 'hate':
        logging.debug(f"{feature_type} score predictions started")
        model = lstm_model()

        graph = tf.get_default_graph()
        with graph.as_default():
            model.load_weights(MODEL_PATH_HATE)
            y_pred = model.predict(vectors)
        y_pred_2 = (y_pred > HATE_THRESHOLD) + 0
        predictions = ['Hate' if i == 1 else 'Non Hate' for i in y_pred_2]
        keras.backend.clear_session()
        preds = [float(i) for i in y_pred]
        res = [{'Label': label, 'Score': score} for label, score in zip(predictions, preds)]
        logging.debug(f"{feature_type} score predictions Successfully")
        return res

