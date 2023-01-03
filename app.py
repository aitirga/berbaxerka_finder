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
    possible_letters = st.text_input('Sartu aukerazko hizkiak jarraian edo koma bidez bananduta')
    if ',' in possible_letters:
        possible_letters = possible_letters.split(',')
    else:
        possible_letters = list(possible_letters)
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
    col1, col2 = st.columns(2)
    chunks = [possible_words[i:i + 100] for i in range(0, len(possible_words), 100)]
    for chunk in chunks:
        col1.write(chunk)
    # Find the word that contains all the letters
    all_letter_words = []
    for word in possible_words:
        intersection = set(word).intersection(set(possible_letters))
        if len(intersection) == len(possible_letters):
            all_letter_words.append(word)
    if len(all_letter_words) > 0:
        col2.write('Guztitzak (hizki denak erabiliz osaturiko hitzak):')
        col2.write(all_letter_words)








