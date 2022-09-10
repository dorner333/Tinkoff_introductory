import argparse
import train as tr

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--prefix", default="", help="Start words")
    parser.add_argument("--model",  default="w2v_model", help="Path to word2vec model saved file")
    parser.add_argument("--length", default=20,  help="Number of words to generate")

    args = parser.parse_args()

    gen = tr.Words_generator()
    gen.generate(args.model, args.length, args.prefix, "dict.pkl")