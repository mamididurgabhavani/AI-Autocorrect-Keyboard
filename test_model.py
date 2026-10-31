
from pathlib import Path
from predict import AutocorrectKeyboard

# Find the training dataset
corpus_path = Path(__file__).parent / "data" / "corpus.txt"

# Create the model
model = AutocorrectKeyboard()

# Train the model
model.train(corpus_path)

# Test next-word prediction
sentence = "i want to drink"

print("\nInput sentence:", sentence)
print("Predicted next words:")

predictions = model.predict_next(sentence)

for word, count in predictions:
    print(f"{word} (count: {count})")

# Test spelling correction
misspelled = "teh"

print("\nOriginal word:", misspelled)
print("Suggested correction:", model.correct_word(misspelled))
