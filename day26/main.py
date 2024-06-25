# NATO phonetic alphabet
import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

codes_dict = {row.letter: row.code for (index, row) in data.iterrows()}


def generate_phonetic():
    word = input("Enter the word: ")
    try:
        list_of_codes = [codes_dict[letter.upper()] for letter in word]
    except KeyError:
        print("Sorry only letters in the alphabet please")
        generate_phonetic()
    else:
        print(list_of_codes)


generate_phonetic()
