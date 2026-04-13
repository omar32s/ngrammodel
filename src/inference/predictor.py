class Predictor:
    def __init__(self,model,normalizer):
        self.NGramModel = model
        self.Normalizer = normalizer

    def normalize(self,text):
        return self.Normalizer.normalize({"user_input":[text]})["user_input"][0].split()
    
    def map_oov(self,context):
        for i,word in enumerate(context):
            if word not in self.NGramModel.vocab:
                context[i] = "<UNK>"
        return context
    
    def predict_next(self,text, k):
        normalized_text = self.normalize(text)
        context = self.map_oov(normalized_text)
        predictions = self.NGramModel.lookup(context)
        return sorted(predictions, key=predictions.get, reverse=True)[:k]
