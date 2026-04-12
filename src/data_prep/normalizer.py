import os
import string

class Normalizer:
    def __init__(self):
        pass
    
    def load(self,folder_path):
        texts = {}

        for filename in os.listdir(folder_path):
            if filename.endswith(".txt"):
                file_path = os.path.join(folder_path, filename)
                
                with open(file_path, "r",encoding="utf-8") as f:
                    texts[filename] = f.readlines()

        return texts
    

    def strip_gutenberg(self,text):
        
        stripped_text = {}

        for key, lines in text.items():
            start_idx = 0
            end_idx = len(lines)

            for i, line in enumerate(lines):
                if "*** START" in line and "GUTENBERG" in line and "\n" in line and " ***" not in line:
                    start_idx = i + 2
                    break

                if "*** START" in line and "GUTENBERG" in line and " ***" in line:
                    start_idx = i + 1
                    break

            for i, line in enumerate(lines):
                if "*** END" in line and "GUTENBERG" in line and "\n" in line and " ***" not in line:
                    end_idx = i
                    break

                if "*** END" in line and "GUTENBERG" in line and " ***" in line:
                    end_idx = i
                    break

            stripped_text[key] = lines[start_idx:end_idx]

        return stripped_text


    def lowercase(self,text):
        lowered_text = {}

        for key, lines in text.items():
            lowered_text[key] = [line.lower() for line in lines]

        return lowered_text

    def remove_punctuation(self,text):
        cleaned_text = {}

        for key, lines in text.items():
            new_lines = []
            for line in lines:
                new_line = ""
                for char in line:
                    if char not in string.punctuation:
                        new_line += char
                new_lines.append(new_line)
            cleaned_text[key] = new_lines

        return cleaned_text

    def remove_numbers(self,text):
        cleaned_text = {}

        for key, lines in text.items():
            new_lines = []
            for line in lines:
                new_line = ""
                for char in line:
                    if not char.isdigit():
                        new_line += char
                new_lines.append(new_line)
            cleaned_text[key] = new_lines

        return cleaned_text
    
    def remove_whitespace(self, text):
        cleaned_text = {}

        for key, lines in text.items():
            new_lines = []
            for line in lines:
               
                stripped_line = ' '.join(line.split())
                
                if stripped_line:
                    new_lines.append(stripped_line)
            cleaned_text[key] = new_lines

        return cleaned_text

    def normalize(self, text):
        cleaned_text = {}
        loweredLoadedData = self.lowercase(text)
        nopuncData = self.remove_punctuation(loweredLoadedData)
        noNumber = self.remove_numbers(nopuncData)
        cleaned_text = self.remove_whitespace(noNumber)
        return cleaned_text
    
    def sentence_tokenize(self, text):
        texts = []
        for textlist in text.values():
            texts.extend(textlist)
        return texts

    def word_tokenize(self,sentence):
        return ' '.join(sentence.split())

    def save(self, sentences, filepath):
        with open(filepath, 'w', encoding='utf-8') as f:
            for sentence in sentences:
                f.write(sentence.strip() + '\n')



def main():
    normalizer = Normalizer()
    loadedData = normalizer.load("E:/AI help/AI help/data/raw/train")
    cleanData = normalizer.normalize(loadedData)
    tokens = normalizer.sentence_tokenize(cleanData)
    normalizer.save(tokens,"E:/AI help/AI help/data/raw/eval/train_tokens.txt")
    strippedLoadedData = normalizer.strip_gutenberg(loadedData)
    loweredLoadedData = normalizer.lowercase(strippedLoadedData)
    nopuncData = normalizer.remove_punctuation(loweredLoadedData)
    noNumber = normalizer.remove_numbers(nopuncData)
    nospacesData = normalizer.remove_whitespace(noNumber)

    for file in nospacesData.keys():
        print(f"{file}================================================================================")
        for line in range(30):
            print(nospacesData[file][line])


if __name__ == "__main__":
    main()