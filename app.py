import streamlit as st
from spylls.hunspell import Dictionary


@st.cache(allow_output_mutation=True)
def load_dictionary():
    dictionary = Dictionary.from_files('./dict/euskara')
    return dictionary


if __name__ == '__main__':
    dictionary = load_dictionary()
    min_length = 3
    st.title('Berbaxerka hitz bilatzailea')
    fixed_letter = st.text_input('Sartu derrigorrezko hizkia')
    possible_letters = st.text_input('Sartu aukerazko hizkiak koma bidez bananduta')
    possible_letters = possible_letters.split(',')
    if fixed_letter not in possible_letters:
        possible_letters.append(fixed_letter)
    fixed_letter = fixed_letter.lower()
    possible_letters = [letter.lower() for letter in possible_letters]

    possible_words = []
    for word in dictionary.dic.words:
        raw_word = word.stem
        if fixed_letter in raw_word:
            get_unique_letters = set(raw_word)
            set_difference = get_unique_letters.difference(set(possible_letters))
            if len(set_difference) == 0:
                if len(raw_word) >= min_length:
                    possible_words.append(raw_word)
    # Delete duplicates
    possible_words = list(set(possible_words))
    possible_words.sort()
    # Make chunks of 100 words
    chunks = [possible_words[i:i + 100] for i in range(0, len(possible_words), 100)]
    for chunk in chunks:
        st.write(chunk)






