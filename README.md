# AI-Autocorrect-Keyboard
The application uses Natural Language Processing (NLP) techniques and an N-gram language model to understand word patterns, suggest corrections, and predict likely next words based on the user's input.
# ⌨️ AI Autocorrect Keyboard

An intelligent keyboard application built using Python and Streamlit that helps users improve their typing experience through **automatic spelling correction and next-word prediction**.

The application uses Natural Language Processing (NLP) techniques and an N-gram language model to understand word patterns, suggest corrections, and predict likely next words based on the user's input.

## 🚀 Features

- **Spelling Correction:** Detects misspelled words and suggests the closest matching words from the vocabulary.
- **Next-Word Prediction:** Predicts the next possible words using unigram, bigram, and trigram models.
- **Text Correction:** Processes complete sentences and corrects recognized spelling mistakes.
- **Interactive Interface:** Provides a simple and user-friendly web interface using Streamlit.
- **Custom Training Dataset:** Learns word patterns from a text corpus.

## 🛠️ Technologies Used

- Python
- Natural Language Processing (NLP)
- Streamlit
- Regular Expressions (Regex)
- Collections (Counter, defaultdict)
- Difflib
- N-gram Language Model

## 🧠 How It Works

The application follows these steps:

1. **Text Preprocessing:** Converts input text into lowercase tokens using regular expressions.
2. **Model Training:** Learns word frequencies and sequential word patterns from the training corpus.
3. **Next-Word Prediction:** Uses unigram, bigram, and trigram frequencies to predict likely next words.
4. **Spelling Correction:** Uses Python's `difflib.get_close_matches()` to find similar words in the vocabulary.
5. **Output Generation:** Displays spelling corrections and next-word suggestions through the Streamlit interface.

## 📂 Project Structure

```text
autocorrect-keyboard/
│
├── app.py                 # Streamlit application
├── predict.py             # NLP prediction and correction logic
├── test_model.py          # Model testing script
│
├── data/
│   └── corpus.txt         # Training dataset
│
├── README.md              # Project documentation
└── requirements.txt       # Project dependencies
```

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/autocorrect-keyboard.git
```

### 2. Navigate to the project directory

```bash
cd autocorrect-keyboard
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

### 4. Activate the virtual environment

**Windows:**

```bash
.venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the application

```bash
streamlit run app.py
```

The application will open in your browser at:

`http://localhost:8501`

## 🧪 Example

**Input:**

```text
i want to drink
```

**Predicted next words:**

- water
- coffee
- tea

**Spelling correction example:**

```text
Input: teh
Output: the
```

*Results depend on the words available in the training vocabulary.*

## 🎯 Learning Outcomes

- Understanding Natural Language Processing fundamentals.
- Implementing unigram, bigram, and trigram language models.
- Learning text preprocessing and tokenization.
- Applying approximate string matching for spelling correction.
- Building an interactive NLP application using Streamlit.

## 🔮 Future Enhancements

- Improve spelling correction accuracy.
- Add context-aware suggestions.
- Implement a clickable virtual keyboard.
- Support multiple languages.
- Explore advanced NLP models for better predictions.

## 👩‍💻 Author

**Durga Bhavani**

B.Tech – Computer Science and Engineering (Cyber Security)

GitHub: [Your GitHub Profile](https://github.com/mamididurgabhavani)

---

⭐ If you find this project interesting, consider giving it a star!
