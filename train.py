import argparse
import pickle
import random
import os
import string

from gensim.models.word2vec import Word2Vec

def save_obj(obj, name):
    with open(name, 'wb') as f:
        pickle.dump(obj, f)


def load_obj(name):
    with open(name, 'rb') as f:
        return pickle.load(f)


def make_pairs(corpus):
    for i in range(len(corpus) - 1):
        yield (corpus[i], corpus[i + 1])


class Words_generator:
    def __init__(self) -> None:
        pass


    def fit(self, data, model_file, dictionary_file):
        file_lst = os.listdir(data)
        corpus = ""
        for file_name in file_lst:
            text = open(os.path.join(data, file_name), encoding = "utf-8").read().lower()
            str_punct = string.punctuation  #Characters to delete
            str_punct += '—' + '»' + '«'
            for p in str_punct:
                if p in text:
                    text = text.replace(p, '')
                if '“' in text:
                    text = text.replace(p, '')
            corpus += text

        corpus = text.split() 

        pairs = make_pairs(corpus)

        word_dict = {}
        for word_1, word_2 in pairs: #creating texts dictionarty
            if word_1 in word_dict.keys():
                word_dict[word_1].append(word_2)
            else:
                word_dict[word_1] = [word_2]
        save_obj(word_dict, dictionary_file)
        
        lst = list()
        lst.append(corpus)
        model = Word2Vec(lst, min_count = 1) #creating w2v model
        model.save(model_file)


    def generate(self, model_file, length, prefix, dictionary_file):
        word_dict = load_obj(dictionary_file)
        model = Word2Vec.load(model_file)
        chain = [prefix] 
        word = prefix.split()[-1] if prefix != "" else ""
        for i in range(int(length)):
            if word in word_dict.keys():
                weights_array = list()
                for word_candidate in set(word_dict[word]):
                    weights_array.append((word_candidate, len(word_candidate) * model.wv.similarity(word_candidate, word)))
                weights_array = sorted(weights_array, key=lambda weight: weight[1])
                if len(weights_array) > 20:
                    word = random.choice(weights_array[-20:-1])[0]
                else:
                    word = random.choice(weights_array)[0]
            else:
                word = random.choice(list(word_dict))
            chain.append(str(word))
        s = ' '.join(chain)
        print(s[0:])

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--inputdir", default="./data/", help="Path to directory with texts")
    parser.add_argument("--model", default="w2v_model", help="Path to word2vec model save file")

    args = parser.parse_args()
    gen = Words_generator()
    gen.fit(args.inputdir, args.model, "dict.pkl")