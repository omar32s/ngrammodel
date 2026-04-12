# main.py
import argparse
import sys
import os
from dotenv import load_dotenv

from src.data_prep.normalizer import Normalizer
from src.model.ngram_model import NGramModel
from src.inference.predictor import Predictor

load_dotenv("config/.env")


K = int(os.getenv("TOP_K"))
TRAIN_FILE= os.getenv("TRAIN_RAW_DIR")
TOKENS_FILE= os.getenv("TRAIN_TOKENS")
MODEL_FILE= os.getenv("MODEL")
VOCAB_FILE= os.getenv("VOCAB")
N= int(os.getenv("NGRAM_ORDER"))


normalizer=Normalizer()
ngrammodel=NGramModel()



def start_dataprep():
    Loaded_data=normalizer.load(TRAIN_FILE)
    Stripped_text=normalizer.strip_gutenberg(Loaded_data)
    Cleaned_data=normalizer.normalize(Stripped_text)
    tokinized_sentences=normalizer.sentence_tokenize(Cleaned_data)
    normalizer.save(tokinized_sentences,TOKENS_FILE)
    print("train_tokens.txt created \n")



def start_model():
    ngrammodel.build_vocab(TOKENS_FILE)
    ngrammodel.save_vocab(VOCAB_FILE)   
    ngrammodel.build_counts_and_probabilities(TOKENS_FILE)
    ngrammodel.save_model(MODEL_FILE) 
    print("model.json and vocab.json created \n")


def start_inference():
    ngrammodel.load(MODEL_FILE,VOCAB_FILE)
    predictor=Predictor(ngrammodel,normalizer)
    print("\n Waiting for User Input... \n")
    try:
        while True:
            text = input("> ").strip()

            if text.lower() in ["quit", "exit"]:
                print("Goodbye")
                break
            if len(text)==0:
                continue
            predictions = predictor.predict_next(text,K)

            print(f"Predictions: {predictions}")

    except KeyboardInterrupt:
        print("\nGoodbye.")
        sys.exit(0)



def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--step",
        choices=["dataprep", "model", "inference", "all"],
        required=True
    )

    args = parser.parse_args()

    if args.step == "dataprep":
        start_dataprep()

    elif args.step == "model":
        start_model()

    elif args.step == "inference":
       start_inference()

    elif args.step == "all":
        start_dataprep()
        start_model()
        start_inference()
        

if __name__ == "__main__":
    main()