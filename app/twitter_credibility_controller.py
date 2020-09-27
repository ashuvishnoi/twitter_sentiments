from flask import Blueprint, request, jsonify
import time
import logging
from configuration import *
from utils.basic_utils import exception_response
from app.twitter_credibility_services import get_twitter_disaster_rating, get_twitter_credibility_rating,\
    get_twitter_hate_rating

logger = logging.getLogger(__name__)


def twitter_credibility_ratings_handler(tk, emb_matrix):

    twitter_disaster_rating = Blueprint('twitter_disaster_rating_api', __name__)
    twitter_hate_rating = Blueprint('twitter_hate_rating_api', __name__)
    twitter_credibility_rating = Blueprint('twitter_credibility_rating_api', __name__)

    @twitter_credibility_rating.route(TWITTER_CREDIBILITY_RATING, methods=['POST'])
    def twitter_credibility_rating_controller():
        try:
            if request.is_json:
                tic = time.time()
                response = get_twitter_credibility_rating(request.get_json(), tk, emb_matrix)

                result = jsonify(response['result'])
                toc = time.time()
                logger.info(f'TIME TAKEN TO GET TWITTER CREDIBILITY RATING: {toc - tic} Secs')
                return result

            else:
                return jsonify(BAD_INPUT)

        except Exception as ex:
            return exception_response(ex)

    @twitter_disaster_rating.route(TWITTER_DISASTER_RATING_ENDPOINT, methods=['POST'])
    def twitter_disaster_controller():
        try:
            if request.is_json:
                tic = time.time()
                response = get_twitter_disaster_rating(request.get_json(), tk[0], emb_matrix[0])

                result = jsonify(response['result'])
                toc = time.time()
                logger.info(f'TIME TAKEN TO GET TWITTER DISASTER RATING: {toc - tic} Secs')
                return result

            else:
                return jsonify(BAD_INPUT)

        except Exception as ex:
            return exception_response(ex)

    @twitter_hate_rating.route(TWITTER_HATE_RATING_ENDPOINT, methods=['POST'])
    def twitter_hate_rating_controller():
        try:
            if request.is_json:
                tic = time.time()
                response = get_twitter_hate_rating(request.get_json(), tk[1], emb_matrix[1])

                result = jsonify(response['result'])
                toc = time.time()
                logger.info(f'TIME TAKEN TO GET TWITTER HATE RATING: {toc - tic} Secs')
                return result

            else:
                return jsonify(BAD_INPUT)

        except Exception as ex:
            return exception_response(ex)

    return twitter_credibility_rating, twitter_disaster_rating, twitter_hate_rating
