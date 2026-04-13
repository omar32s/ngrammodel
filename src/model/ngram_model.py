
import json

class NGramModel:
    def __init__(self):
        self.vocab = []
        self.model = {}

    def build_vocab(self,token_file):
        veco = {}
        with open(token_file, 'r', encoding='utf-8') as f:
            content = f.readlines()
        
        for line in content:
            words = line.split()
            for word in words:
                if word not in veco:
                    veco[word] = 0
                veco[word] += 1

        for word in veco.keys():
            if veco[word] > UNK_THRESHOLD:
                self.vocab.append(word)

        return self.vocab


    def build_counts_and_probabilities(self, token_file):
        tokens = []
        with open(token_file, "r", encoding="utf-8") as f:
            content = f.readlines()

        for line in content:
            words = line.split()
            for word in words:
                if word not in self.vocab:
                    word = "<UNK>"
                tokens.append(word)
    
        counts = {}

        for i in range(len(tokens)):
            for order in range(1, NGRAM_ORDER + 1):
                if i < order - 1:
                    continue
                context = " ".join(tokens[i - order + 1 : i])
                target  = tokens[i]

                if context not in counts:
                    counts[context] = {}
                if target not in counts[context]:
                    counts[context][target] = 0
                counts[context][target] += 1
        
        for context, targets in counts.items():
            total = sum(targets.values())
            self.model[context] = {word: count / total for word, count in targets.items()}
        
    def save_model(self,model_path): 
        with open(model_path, 'w', encoding='utf-8') as f:
            json.dump(self.model, f, ensure_ascii=False, indent=4)
            
    def save_vocab(self,vocab_path):
        with open(vocab_path, 'w', encoding='utf-8') as f:
            json.dump(self.vocab, f, ensure_ascii=False, indent=4)
    
    def load(self,model_path, vocab_path):
        with open(model_path, 'r', encoding='utf-8') as f:
            self.model = json.load(f)
        with open(vocab_path, 'r', encoding='utf-8') as f:
            self.vocab = json.load(f)

    def lookup(self,context):
        if len(context) > NGRAM_ORDER - 1:
            startingContextSize = NGRAM_ORDER - 1
        else:
            startingContextSize = len(context)
        
        for i in range(startingContextSize, 0, -1):
            if " ".join(context[-i:]) in self.model.keys():
                context_str = " ".join(context[-i:])
                predictions = self.model[context_str]
                return predictions
        return {}


def main():
    
if __name__ == "__main__":
    main()
