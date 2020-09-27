from configuration import *
import logging
logger = logging.getLogger(__name__)
from app.twitter_credibility_core import twitter_disaster_rating, twitter_hate_rating, twitter_credibility_rating


def get_twitter_credibility_rating(input_obj, tk, emb_matrix):
    try:

        tweets_data = twitter_credibility_rating(input_obj, tk, emb_matrix)
        response = create_response_object(len(tweets_data), tweets_data, STATUS_SUCCESS)
        return response

    except Exception as ex:
        logger.exception("Error: {}".format(ex))
        response = create_response_object(STATUS_FAILED, [], NEWS_CREDIBILITY_RATING_FAILED)
        return response


def get_twitter_disaster_rating(input_obj, tk, emb_matrix):
    try:
        text = input_obj.get('text', [''])

        tweets_data = twitter_disaster_rating(text, tk, emb_matrix)
        response = create_response_object(len(tweets_data), tweets_data, STATUS_SUCCESS)
        return response

    except Exception as ex:
        logger.exception("Error: {}".format(ex))
        response = create_response_object(STATUS_FAILED, [], NEWS_CREDIBILITY_RATING_FAILED)
        return response


def get_twitter_hate_rating(input_obj, tk, emb_matrix):
    try:
        text = input_obj.get('text', [''])

        tweets_data = twitter_hate_rating(text, tk, emb_matrix)
        response = create_response_object(len(tweets_data), tweets_data, STATUS_SUCCESS)
        return response

    except Exception as ex:
        logger.exception("Error: {}".format(ex))
        response = create_response_object(STATUS_FAILED, [], NEWS_CREDIBILITY_RATING_FAILED)
        return response


def create_response_object(len_data, data, message):
    """
    Function to create a standard response object for sending back to request.
    """
    if len_data != 0:
        response = {'status': STATUS_SUCCESS, 'message': message,
                    'result': data}
        logger.info(message)
        return response

    else:
        response = {'status': STATUS_FAILED, 'message': NEWS_CREDIBILITY_RATING_FAILED,
                    'result': {}}
        logger.info(NEWS_CREDIBILITY_RATING_FAILED)
        return response
