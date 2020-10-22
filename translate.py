from translate import Translator
print("Welcome to the English to Spanish Translator!\n")
sentence = input("Please enter a sentence: ")

try:
    with open("newFile.txt", mode = 'w') as my_file:
        my_file.write(sentence) 
except IOError as err:
    print("Wrong syntax")

try: 
    with open("newFile.txt") as my_file:
        Sentence = my_file.read()
        translator= Translator(to_lang="es")
        translatedSentence = translator.translate(Sentence)
        print(translatedSentence)
except FileNotFoundError as err:
    print("error")
