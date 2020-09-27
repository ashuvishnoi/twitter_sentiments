AWS = True
if AWS:
    TOKENIZER_DISASTER_PATH = '/home/ubuntu/pretrain_files/twitter_pretrain_files/tokenizer_disaster.pkl'
    TOKENIZER_HATE_PATH = '/home/ubuntu/pretrain_files/twitter_pretrain_files/tokenizer_hate.pkl'
    WORD2VEC_PATH = '/home/ubuntu/pretrain_files/twitter_pretrain_files/b2b_twitter_w2v'
    MODEL_PATH_DISASTER = '/home/ubuntu/pretrain_files/twitter_pretrain_files/twitter_disaster.h5'
    MODEL_PATH_HATE = '/home/ubuntu/pretrain_files/twitter_pretrain_files/twitter_hate.h5'
else:
    TOKENIZER_DISASTER_PATH = ''
    TOKENIZER_HATE_PATH = ''
    GLOVE_EMB_PATH = ''
    RNN_PATH_DISASTER = ''
    RNN_PATH_HATE = ''


# endpoints
TWITTER_DISASTER_RATING_ENDPOINT = '/twitter/rating/disaster'
TWITTER_HATE_RATING_ENDPOINT = '/twitter/rating/hate'
TWITTER_CREDIBILITY_RATING = '/twitter/rating/all'


# text_utils
BAD_INPUT = 'Bad Input , Only Json format excepted'
STATUS_SUCCESS = "OK"
STATUS_FAILED = "ERROR"
NEWS_CREDIBILITY_RATING_FAILED = "News credibility rating failed."
ERROR_EXCEPTION_OCCUR = "An exception of type {0} occurred. Arguments:\n{1!r}"

maxlen = 20
# nb_words_disaster = 17876
# nb_words_hate = 9447
EMBEDDING_DIM = 300

# thresholds
DISASTER_THRESHOLD = 0.5
HATE_THRESHOLD = 0.5


# params
hate_param = 0.30
disaster_param = 0.45
neg_opinion_param = 0.25
