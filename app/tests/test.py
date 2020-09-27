from app.twitter_credibility_core import twitter_credibility_rating
import pickle
from configuration import  TOKENIZER_DISASTER_PATH, TOKENIZER_HATE_PATH
from app import make_emb_matrix_disaster, make_emb_matrix_hate


with open(TOKENIZER_DISASTER_PATH, 'rb') as tokenizer:
    tk_disaster = pickle.load(tokenizer)

with open(TOKENIZER_HATE_PATH, 'rb') as tokenizer:
    tk_hate = pickle.load(tokenizer)

tk = (tk_disaster, tk_hate)


def test_twitter_credibility_rating():
    obj = [{'text': 'if the world was ending ma was determined to be together with her entire family when it happened so she told her father to book her tickets to delhi & amp nothing could change her mindthey say that the winter of 61 62 was really cold but i dont think my parents felt the chill',
               'title': ''}]
    embb_matrix = (make_emb_matrix_disaster(), make_emb_matrix_hate())
    res = twitter_credibility_rating(obj, tk, embb_matrix)
    expected_output = [{'INDIVIDUAL_SCORES': {'client_name': '',
   'disaster': {'Label': 'Non Disaster', 'Score': 0.2529498338699341},
   'hate': {'Label': 'Non Hate', 'Score': 0.3448248505592346},
   'query_name': '',
   'sentiment_polarity': 0.3,
   'source_url': '',
   'text': 'if the world was ending ma was determined to be together with her entire family when it happened so she told her father to book her tickets to delhi & amp nothing could change her mindthey say that the winter of 61 62 was really cold but i dont think my parents felt the chill',
   'time_stamp_utc': ''},
  'OVERALL_CREDIBILITY_SCORE': {'Credibility_Score': 0.2922748804092407,
   'original_text': '',
   'text': 'if the world was ending ma was determined to be together with her entire family when it happened so she told her father to book her tickets to delhi & amp nothing could change her mindthey say that the winter of 61 62 was really cold but i dont think my parents felt the chill'}}]

    assert res == expected_output
