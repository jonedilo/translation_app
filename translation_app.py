import streamlit as st
from googletrans import Translator


def translate_text(text, source_lang, target_lang):
    translator = Translator()
    translated_text = translator.translate(text, src=source_lang, dest=target_lang)
    return translated_text.text

def main():
    st.title("Multilingual Text Translation App")
 # Load Google API credentials
    credentials_path = "YOUR_GOOGLE_CREDENTIALS_JSON_FILE.json"
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credentials_path
    st.sidebar.header("Settings")
    source_lang = st.sidebar.selectbox("Select Source Language", ("en", "es", "fr", "de", "ja"))
    target_lang = st.sidebar.selectbox("Select Target Language", ("en", "es", "fr", "de", "ja"))
    text = st.text_area("Enter Text to Translate")
    if st.button("Translate"):
        if text:
            translated_text = translate_text(text, source_lang, target_lang)
            st.write("Translated Text:")
            st.write(translated_text)
        else:
            st.write("Please enter text to translate.")


if __name__ == "__main__":
    main()
