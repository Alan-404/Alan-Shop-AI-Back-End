from keras.models import load_model
from keras_preprocessing.sequence import pad_sequences
import pickle
import io
import re

class PasswordCheckService:
    def __init__(self, max_length=50, model_folder = "./password_check/saved_models/model.h5", tokenizer_folder = "./password_check/tokenizer/tokenizer.pickle"):
        self.max_length = max_length
        self.model = load_model(model_folder)
        with io.open(tokenizer_folder, 'rb') as handle:
            self.tokenizer = pickle.load(handle)
    def preprocessing(self, sequence: str):
        lst = []
        for item in sequence:
            lst.append(item)
        sentence = " ".join(lst)
        input_pred = self.tokenizer.texts_to_sequences([sentence])
        return pad_sequences(input_pred, maxlen=self.max_length, padding='post', truncating='post')
    def predict(self, input_sequence: str):
        input_sequence = re.sub('\s', '', input_sequence)
        if (input_sequence == ""):
            return 0
        sequence_processed = self.preprocessing(input_sequence)
        return self.model.predict(sequence_processed).argmax()