import json
from konlpy.tag import Okt
import pandas as pd
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding



okt = Okt()

def tokenizer(x_data) :
    text_results = []
    for text in x_data:
        token = okt.pos(text, norm=True, stem=True)
        word = []
        for w in token:
            if not w[1] in ["Josa", "Eomi", "Punctuation"]:
                word.append(w[0])
        rl = (" ".join(word)).strip()
        text_results.append(rl)

    prep_file = "train_docs.json"
    with open(prep_file, 'w', encoding='utf-8') as make_file:
        json.dump(text_results, make_file, ensure_ascii=True)

    tokens = [t for d in text_results for t in d]
    print(len(tokens))

    return text_results

def token2vec(text_results):
    vocab_size = 1000
    tokenizer = Tokenizer(num_words=vocab_size)
    tokenizer.fit_on_texts(text_results)
    sequence = tokenizer.texts_to_sequences(text_results)
    print(sequence)

    return sequence
'''
    model = Sequential()
    model.add(Embedding(vocab_size, 4))
'''


