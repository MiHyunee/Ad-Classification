import json
from konlpy.tag import Okt
import pandas as pd
from tensorflow.keras.preprocessing.text import Tokenizer

okt = Okt()

def tokenizer() :
    text_results = []

    #data load
    dwn_url = "/Users/software/Downloads/dataSet.csv"
    data = pd.read_csv(dwn_url, error_bad_lines=False, encoding='utf-8', header=0)
    print("총 샘플 수 : ", len(data))

    data['class'] = data['class'].replace(['none', 'ad'], [0, 1])
    data.drop_duplicates(subset='문장', inplace=True)

    #data x,y로 나누기
    x_data = data['문장']
    y_data = data['class']
    print('text 수:', len(x_data))
    print('class 수: ', len(y_data))

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

    #tokens = [t for d in text_results for t in d]
    #print(len(tokens))

    return text_results, y_data

def token2vec(text_results):
    vocab_size = 1000
    tokenizer = Tokenizer(num_words=vocab_size)
    tokenizer.fit_on_texts(text_results)
    sequence = tokenizer.texts_to_sequences(text_results)
    #print(sequence)

    return sequence


