import argparse
import train as tr

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--prefix", default="", help="word to start")
    parser.add_argument("--model",  default="w2v_model", help="This is the path to the file with model")
    parser.add_argument("--length", default=20,  help="number of words to generate")

    args = parser.parse_args()

    gen = tr.TextGen()
    gen.generate(args.model, args.length, args.prefix, "dict.pkl")