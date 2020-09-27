from keras.layers import Dense, Input, Flatten, Embedding, BatchNormalization, Dropout, LSTM
from keras.models import Model
from configuration import maxlen, EMBEDDING_DIM


def lstm_model():
    """
    Model definiton for CPU
    :param nb_words: int-Number of words in embedding layer
    :return: Model
    """

    inp = Input(shape=(maxlen, EMBEDDING_DIM))
    # layer = Embedding(nb_words, 200, trainable=False, weights = [embedding_matrix])(inp)
    layer = LSTM(100, return_sequences=True)(inp)

    layer = Flatten()(layer)
    layer = Dense(50, activation="relu")(layer)
    layer = Dropout(0.40)(layer)
    layer = Dense(10, activation="relu")(layer)
    layer = BatchNormalization()(layer)
    layer = Dense(5, activation="relu")(layer)

    layer = Dense(1, activation="sigmoid")(layer)
    model = Model(inputs=inp, outputs=layer)
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
    return model


# model = rnn_model(embedding_matrix)
