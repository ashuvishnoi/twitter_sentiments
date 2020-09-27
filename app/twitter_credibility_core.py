import logging
from app.twitter_credibility_ratings_operations.clean import cleaning_of_texts
from app.twitter_credibility_ratings_operations.vectorization import convert_into_vectors_disaster,\
    convert_into_vectors_hate
from app.twitter_credibility_ratings_operations.predict import predict
import numpy as np
from textblob import TextBlob
from configuration import disaster_param, hate_param, neg_opinion_param
from app.decorators.decorators import timed, memory_profile


def make_rating_obj(text, predictions, feature_type):
    response = [{'text': text_sample, 'prediction': pred, 'feature_type': feature_type}
                for text_sample, pred in zip(text, predictions)]
    return response


def make_full_object(disaster_obj, hate_obj, obj):
    disaster = disaster_obj.get('prediction', '')
    hate = hate_obj.get('prediction', '')
    text = disaster_obj.get('text', '')
    time = obj.get('time_stamp_utc', '')
    client = obj.get('client_name', '')
    query = obj.get('query_name', '')
    url = obj.get('source_url', '')
    original_text = obj.get('original_text', '')
    sentiment_polarity = text_sentiment(text)
    cred_score = disaster_param * disaster.get('Score') + hate_param * hate.get('Score') + neg_opinion_param * sentiment_polarity
    # cred_score = (1 - np.mean(np.array([disaster.get('Score'), hate.get('Score'), sentiment_polarity])))
    response_obj1 = {'Credibility_Score': cred_score, 'text': text, 'original_text': original_text}
    response_obj2 = {'text': text, 'disaster': disaster, 'hate': hate, 'time_stamp_utc': time, 'client_name': client,
                     'query_name': query, 'source_url': url, 'sentiment_polarity': sentiment_polarity}
    res_obj = {'OVERALL_CREDIBILITY_SCORE': response_obj1, 'INDIVIDUAL_SCORES': response_obj2}
    return res_obj


def text_sentiment(text):

    value = TextBlob(text).sentiment.polarity
    if value < 0:
        value = abs(value)
    else:
        value = 0

    return value


@timed
@memory_profile
def twitter_credibility_rating(objects, tk, embb_matrix):
    '''
    Fn to get news credibility rating object
    :param text: list of texts(string)
    :param feature_type: feature type to predict
    :return: list of credibility rating objects
    '''
    text = [obj.get('text', '') for obj in objects]
    queries = [obj.get('query_name', '') for obj in objects]
    logging.info(f'twitter credibility rating started for queries = {queries}')
    disaster = twitter_disaster_rating(text, tk[0], embb_matrix[0])
    hate = twitter_hate_rating(text, tk[1], embb_matrix[1])
    response = [make_full_object(disaster_obj, hate_obj, obj)
                for disaster_obj, hate_obj, obj in zip(disaster, hate, objects)]
    logging.info(f'twitter credibility ratings got successfully for queries = {queries}')
    return response


@timed
@memory_profile
def twitter_disaster_rating(text, tk, embb_matrix):
    logging.info('twitter_disaster_rating started')
    feature_type = 'disaster'
    cleaned_text = cleaning_of_texts(text)
    vectors_of_text = convert_into_vectors_disaster(cleaned_text, tk, embb_matrix)
    disaster_predictions = predict(vectors_of_text, feature_type)
    response = make_rating_obj(text, disaster_predictions, feature_type)
    logging.info('twitter_disaster_rating successfully')
    return response


@timed
@memory_profile
def twitter_hate_rating(text, tk, embb_matrix):
    logging.info('twitter_hate_rating started')
    feature_type = 'hate'
    cleaned_text = cleaning_of_texts(text)
    vectors_of_text = convert_into_vectors_hate(cleaned_text, tk, embb_matrix)
    hate_predictions = predict(vectors_of_text, feature_type)
    response = make_rating_obj(text, hate_predictions, feature_type)
    logging.info('twitter_disaster_rating successfully')
    return response
