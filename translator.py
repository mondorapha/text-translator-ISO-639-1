'''
Little app to translate text files to every language listed under
ISO 639-1 codes. Language has to be specified following the same format.
'''

from translate import Translator

chosen_lang = input('Which language to translate to (ISO 639-1 format): ')
translator = Translator(to_lang=chosen_lang)

try:
    with open('./resources/text.txt', mode='r', encoding='UTF-8') as o_text:
        original = o_text.read()
        print(original)
        translation = translator.translate(original)
        print(translation)
        with open('./resources/translated-text.txt', mode='w', encoding='UTF-8') as t_text:
            t_text.write(translation)
except FileNotFoundError as err1:
    print('Sorry, file not found.')
    raise err1
except IOError as err2:
    print('IO error.')
    raise err2
