
import streamlit as st
from pathlib import Path
from predict import AutocorrectKeyboard

st.set_page_config(
    page_title="AI Autocorrect Keyboard",
    page_icon="⌨️",
    layout="centered"
)

st.title("⌨️ AI Autocorrect Keyboard")
st.write("Predict your next word and improve your spelling.")

@st.cache_resource
def load_model():
    model = AutocorrectKeyboard()
    corpus_path = Path(__file__).parent / "data" / "corpus.txt"
    model.train(corpus_path)
    return model

try:
    model = load_model()

    sentence = st.text_area(
        "Type your sentence",
        placeholder="Example: i want to drink teh",
        height=120
    )

    if st.button("Predict and Correct", type="primary"):
        if sentence.strip():
            st.subheader("Next-word suggestions")
            predictions = model.predict_next(sentence)

            if predictions:
                words = [word for word, count in predictions]
                st.write(" · ".join(words))
            else:
                st.info("No next-word suggestions found.")

            st.subheader("Spelling correction")
            corrected_words = []

            for word in sentence.split():
                corrected = model.correct_word(word)
                corrected_words.append(corrected)

            st.write(" ".join(corrected_words))
        else:
            st.warning("Please type a sentence first.")

except Exception as error:
    st.error(f"Could not load the model: {error}")
