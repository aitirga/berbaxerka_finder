from spylls.hunspell import Dictionary
import unidecode

if __name__ == '__main__':
    dictionary = Dictionary.from_files('./dict/euskara')


    for word in dictionary.dic.words:
        pass
