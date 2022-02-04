import translate

translator = translate.Translator(to_lang='hi')

try:
    with open('Python File I_O/translation.txt', mode='r') as translate:
        tranlate_into = translate.read()
        translation = translator.translate(tranlate_into)
        with open('Python File I_O/translation1.txt', mode='w') as translate1:
            translate1.write(translation)
except FileNotFoundError as err:
    print('File is not there')

'''
Update the programme and make it a terminal based user friendly apps.
'''
