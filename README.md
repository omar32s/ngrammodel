# N-Gram Next Word Predictor

A Python-based N-Gram language model designed to predict the next word in a sequence. This project specifically targets text data from Project Gutenberg (e.g., Sherlock Holmes stories), providing a full pipeline from raw text normalization to interactive inference.

## Project Structure

```text
ngram-predictor/
├── config/
│   └── .env                # Environment variables and model configuration
├── data/
│   ├── raw/                # Source text files (e.g., Gutenberg books)
│   └── processed/          # Cleaned tokens used for training
├── src/
│   ├── data_prep/          # Text cleaning and normalization logic
│   ├── model/              # N-Gram counting and probability calculation
│   └── inference/          # Prediction logic for user input
├── main.py                 # CLI entry point
└── README.md
```

## Setup

1. **Environment Variables**:
   Ensure you have a `.env` file located in `config/.env`. It should define the following parameters:
   ```env
   TOP_K=3
   TRAIN_RAW_DIR=data/raw/train/
   TRAIN_TOKENS=data/processed/train_tokens.txt
   MODEL=models/model.json
   VOCAB=models/vocab.json
   NGRAM_ORDER=3
   ```

2. **Data**:
   Place your raw text files (Gutenberg format) into the directory specified by `TRAIN_RAW_DIR`.

## Usage

The project is controlled via `main.py` using the `--step` argument.

### 1. Data Preparation
Cleans raw text, strips Gutenberg headers/footers, normalizes casing/punctuation, and tokenizes sentences.
```bash
python main.py --step dataprep
```

### 2. Build Model
Constructs the vocabulary and calculates N-Gram counts and probabilities based on the processed tokens.
```bash
python main.py --step model
```

### 3. Run Inference
Starts an interactive loop where you can enter text and receive the top-K suggested next words.
```bash
python main.py --step inference
```

### 4. Run Entire Pipeline
Executes data prep, model building, and starts inference in one go.
```bash
python main.py --step all
```

## Interactive Commands
During inference, type your phrase to see predictions. Type `exit` or `quit` to stop the program.
