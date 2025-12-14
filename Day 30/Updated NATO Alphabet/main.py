import pandas 
letter_data_frame = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dic = {row.letter: row.code for (index, row) in letter_data_frame.iterrows()}

def text_to_phonetic_alphabet():
    word = input("Enter a word: ").upper()
    try:
        output_list = [phonetic_dic[letter] for letter in word] 
        print(output_list)
    except KeyError:
        print("Sorry, only letters in  the alphabet please.")
        text_to_phonetic_alphabet()

text_to_phonetic_alphabet()
