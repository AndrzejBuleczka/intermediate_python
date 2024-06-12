# NATO phonetic alphabet
import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

codes_dict = {row.letter: row.code for (index, row) in data.iterrows()}

list_of_codes = [codes_dict[letter.upper()] for letter in input("Enter the word: ")]
print(list_of_codes)